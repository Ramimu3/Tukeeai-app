import os
import pypdf
from ebooklib import epub
from bs4 import BeautifulSoup
from django.conf import settings
from .models import UploadedFile
from .crew_ai import QuestionGenerationCrew  # Adjust the import path as needed
from django.contrib.auth.models import User  # Import the User model
import re
import csv

# processing.py
def extract_text_from_file(file_path):
    if file_path.lower().endswith('.pdf'):
        text, num_pages = extract_text_from_pdf(file_path)
        return text, True, num_pages  # Return text, is_pdf=True, and num_pages
    elif file_path.lower().endswith('.epub'):
        text = extract_text_from_epub(file_path)
        return text, False, 0  # Return text, is_pdf=False, and 0 for num_pages
    else:
        raise ValueError("Unsupported file format")
    
def extract_text_from_pdf(pdf_path):
    reader = pypdf.PdfReader(pdf_path)
    text = ""
    for page in reader.pages:
        text += page.extract_text() if page.extract_text() else ""
    num_pages = len(reader.pages)
    return text, num_pages

import ebooklib

def extract_text_from_epub(epub_path):
    book = ebooklib.epub.read_epub(epub_path)
    text = ""
    for item in book.get_items_of_type(ebooklib.ITEM_DOCUMENT):
        soup = BeautifulSoup(item.content, 'html.parser')
        text += soup.get_text()
    return text

def save_chunks_to_files(chunks, base_name, output_dir="chunks"):
    os.makedirs(output_dir, exist_ok=True)
    for i, chunk in enumerate(chunks, start=1):
        filename = os.path.join(output_dir, f"{base_name}_chunk_{i}.txt")
        with open(filename, 'w', encoding='utf-8') as file:
            file.write(chunk)
        print(f"Saved: {filename}")

def adjust_chunk_end(text, start, end):
    nearest_period = text.rfind('.', start, end)
    nearest_question = text.rfind('?', start, end)
    nearest_exclamation = text.rfind('!', start, end)
    new_end = max(nearest_period, nearest_question, nearest_exclamation) + 1
    return new_end if new_end > start else end

def split_text_into_chunks(text, is_pdf=False, num_pages=0):
    if is_pdf and num_pages > 0:
        num_chunks = max(num_pages // 3, 1)
    else:
        avg_words_per_page = 300
        words = text.split()
        estimated_pages = len(words) // avg_words_per_page
        num_chunks = max(estimated_pages // 3, 1)

    total_length = len(text)
    chunk_size = total_length // num_chunks
    chunks = []
    start = 0
    for i in range(num_chunks):
        end = start + chunk_size
        if i < num_chunks - 1:
            end = adjust_chunk_end(text, start, end)
        else:
            end = len(text)
        chunks.append(text[start:end])
        start = end

    return chunks

def convert_and_split(file_id, user_id):
    try:
        uploaded_file = UploadedFile.objects.get(id=file_id)
        user = User.objects.get(id=user_id)

        file_path = os.path.join(settings.MEDIA_ROOT, uploaded_file.file.name)
        text, is_pdf, num_pages = extract_text_from_file(file_path)
        chunks = split_text_into_chunks(text, is_pdf, num_pages)
        
        base_name = os.path.splitext(os.path.basename(file_path))[0]
        user_specific_dir = os.path.join('chunks', str(user.username))
        output_dir = os.path.join(settings.MEDIA_ROOT, user_specific_dir, str(file_id))
        
        save_chunks_to_files(chunks, base_name, output_dir)
        return output_dir
    except (UploadedFile.DoesNotExist, User.DoesNotExist):
        raise ValueError("File or User not found.")
    
def run_crew_ai(chunks_path, user_id):
    """
    Processes each text chunk with Crew AI and saves the output in a user-specific folder.
    Adjusted to directly handle string outputs from Crew AI processing.

    :param chunks_path: Path to the directory containing the text chunks.
    :param user_id: ID of the user who initiated the process.
    """
    # Directory for Crew AI outputs, nested within the user-specific directory
    output_dir = os.path.join(chunks_path, f"user_{user_id}_crew_ai_outputs")
    os.makedirs(output_dir, exist_ok=True)
    
    chunk_files = [os.path.join(chunks_path, f) for f in os.listdir(chunks_path) if os.path.isfile(os.path.join(chunks_path, f))]
    for chunk_file in chunk_files:
        with open(chunk_file, 'r', encoding='utf-8') as file:
            chunk_text = file.read()
        
        # Adjusted to pass text directly to Crew AI
        question_generation_crew = QuestionGenerationCrew([chunk_text])
        base_name = os.path.join(output_dir, os.path.basename(chunk_file).replace("_chunk_", "_crew_ai_output"))
        question_generation_crew.run(base_name)  # Crew AI output is directly saved to file

    return output_dir

def check_mistakes(crew_ai_output):
    # Placeholder for logic to check for any mistakes in the Crew AI output
    pass

def dynamic_remove_line_numbers(text):
    return re.sub(r'^\s*\d+\.\s*', '', text, flags=re.MULTILINE)

def preprocess_data(text):
    """Preprocess text by removing specific prefixes and formatting."""
    removal_patterns = [
        r"^\*\*Question\*\*:\s*", r"^\*\*Answer\*\*:\s*",
        r"^Question\*\*:\s*", r"^Answer\*\*:\s*",
        r"^\*\*Question\s+\d+\*\*:\s*", r"^\*\*Answer\s+\d+\*\*:\s*",
        r"^\*\*Question\s+One\*\*:\s*", r"^Answer\s+One:\s*",
        r"^Question\s+\d+:\s*", r"^Answer\s+\d+:\s*",
        r"^Answer to question#\d+:\s*",
        r"^\d+\)\s*", r"^Question\s+\d+\):\s*", r"^Answer\s+\d+\):\s*",
        r"^Question:\s*", r"^Answer:\s*",
        r"^\*\*Question:\*\*\s*", r"^\*\*Answer:\*\*\s*",
        r"Question\s*\d*\):?\s*", r"Answer\s*\d*\):?\s*",
        r"\*\*Question\s*\d*\*\*:?\s*", r"\*\*Answer\s*\d*\*\*:?\s*",
        # Catch all variants of "Question" and "Answer" labels, with or without numbering and markdown styling
        r"^\*\*?Question(\s+\d+| One)?\*\*?:?\s*", r"^\*\*?Answer(\s+\d+| to question#\d+| One)?\*\*?:?\s*",
        # Handling "Answer to question#25:" or similar patterns
        r"Answer to question#\d+:\s*",
                # Handle cases with leading dashes or markdown headers before Question/Answer
        r"^-+\s*\*\*?Question\*\*?:?\s*", r"^-+\s*\*\*?Answer\*\*?:?\s*",
        r"^#+\s*\*\*?Question\*\*?:?\s*", r"^#+\s*\*\*?Answer\*\*?:?\s*",
        # General patterns for "Question:" and "Answer:", including markdown and numbers
        r"^\*\*?Question(\s+\d+| One)?\*\*?:?\s*", r"^\*\*?Answer(\s+\d+| to question#\d+| One)?\*\*?:?\s*",
        # Specific patterns for handling numbering and markdown styling
        r"^(\*\*)?Question\s*\d*(\*\*):?\s*", r"^(\*\*)?Answer\s*\d*(\*\*):?\s*",
        # Additional patterns for "Question 9:", "### Question 1:", etc.
        r"^(\*\*)?Question\s+\d+:\s*", r"^(\*\*)?Answer\s+\d+:\s*",
        # Catch all variants of "Question" and "Answer" labels, with special markdown headers or dashes
        r"^-+\s*Question:\s*", r"^-+\s*Answer:\s*",
        r"^#+\s*Question:\s*", r"^#+\s*Answer:\s*",
        # Patterns for "Answer to question#25:" or similar
        r"Answer to question#\d+:\s*",
        # Clean-up for orphaned markdown or numerical list items
        r"^\d+\)\s*", r"^-+\s*", r"^#+\s*",
                # Directly addressing cases like "Question 50:" or "Answer 50:", including markdown bold
        r"^\**Question\s+\d*:*[\*\s]*", r"^\**Answer\s+\d*:*[\*\s]*",
        # Handling cases with leading dashes, markdown headers, or markdown bold around "Question" or "Answer"
        r"^-+\s*\**Question\**:\s*", r"^-+\s*\**Answer\**:\s*",
        r"^#+\s*\**Question\**:\s*", r"^#+\s*\**Answer\**:\s*",
        # Removing markdown bold syntax "**" around "Question" or "Answer" with optional numbering
        r"^\*\*Question(\s+\d+)?\*\*:\s*", r"^\*\*Answer(\s+\d+)?\*\*:\s*",
        # General clean-up for any remaining markdown syntax or numerical list items
        r"^-+\s*", r"^#+\s*", r"^\d+\)\s*",
        # Additional patterns for specific cases mentioned
        r"^\*\*?Question(\s+\d+| One)?\*\*?:?\s*", r"^\*\*?Answer(\s+\d+| to question#\d+| One)?\*\*?:?\s*",
        r"Answer to question#\d+:\s*",
                # Handling bold markdown "**Question:**" and "**Answer:**" directly
        r"^\*\*Question:\*\*\s*", r"^\*\*Answer:\*\*\s*",
        # Handling cases with optional markdown bold "**", digits, and optional colon ":", followed by any spaces
        r"^\**Question\s*\d*\**:*[\s]*", r"^\**Answer\s*\d*\**:*[\s]*",
        # Removing cases with leading dashes "-" or markdown headers "#"
        r"^-+\s*\**Question\**:\s*", r"^-+\s*\**Answer\**:\s*",
        r"^#+\s*\**Question\**:\s*", r"^#+\s*\**Answer\**:\s*",
        # General clean-up for any markdown syntax, numerical list items, or spaces
        r"^-+\s*", r"^#+\s*", r"^\d+\)\s*",
        # Ensuring removal of "Question:" and "Answer:" labels with flexible handling for numbering and markdown
        r"^\*\*?Question(\s+\d+| One)?\*\*?:?\s*", r"^\*\*?Answer(\s+\d+| to question#\d+| One)?\*\*?:?\s*",
        r"Answer to question#\d+:\s*",
                # Targeting leading asterisk possibly followed by spaces, then **Question:** or **Answer:** with optional bold markdown
        r"^\*+\s*\*\*Question:\*\*\s*", r"^\*+\s*\*\*Answer:\*\*\s*",
        # Handling optional leading asterisks, optional markdown bold "**", digits, and optional colon ":", followed by any spaces
        r"^\*+\s*\**Question\s*\d*\**:*[\s]*", r"^\*+\s*\**Answer\s*\d*\**:*[\s]*",
        # Removing cases with leading dashes "-" or markdown headers "#"
        r"^-+\s*\**Question\**:\s*", r"^-+\s*\**Answer\**:\s*",
        r"^#+\s*\**Question\**:\s*", r"^#+\s*\**Answer\**:\s*",
        # General clean-up for any remaining markdown syntax, numerical list items, or extra asterisks
        r"^-+\s*", r"^#+\s*", r"^\d+\)\s*", r"^\*+\s*",
        # Ensuring removal of "Question:" and "Answer:" labels with flexible handling for numbering and markdown
        r"^\*\*?Question(\s+\d+| One)?\*\*?:?\s*", r"^\*\*?Answer(\s+\d+| to question#\d+| One)?\*\*?:?\s*",
        r"Answer to question#\d+:\s*",
                # Directly target "**Answer:**", "*Answer*:", and "Answer:" with optional leading spaces or asterisks
        r"^\*+\s*\*Answer\*:\s*", r"^\*+\s*Answer:\s*",
        # Targeting variations with numerical identifiers, bold markdown, and optional colons
        r"^\*\*?Answer\s*(\d+)?\*\*?:?\s*",
        # Handling leading special characters or markdown headers before "Answer"
        r"^-+\s*\*\*?Answer\*\*?:?\s*", r"^#+\s*\*\*?Answer\*\*?:?\s*",
        # Clean-up for general patterns, including markdown syntax or numerical list items
        r"^-+\s*", r"^#+\s*", r"^\d+\)\s*",
        # Specific cleanup for "Answer to question#25:" or similar patterns
        r"Answer to question#\d+:\s*",
        r"^\*?_?Answer:?_?\*?\s*",
        r"^A\)\s*",
        r"^Q\d+\)\s*",
        r"^Answer:?\s*",
        r"^Answer \(using exact quote from the text\):\s*",
        r"^Answer \(using exact quote\):\s*",
        r"^Answer \d+:\s*",
        r"^\*?_?Answer:?_?\*?\s*",
        r"^A\)\s*",
        r"^Q\d+\)\s*",
        r"^Answer:?\s*",
        r"^Answer \(using exact quote from the text\):\s*",
        r"^Answer \(using exact quote\):\s*",
        r"^Answer \d+:\s*",
    ]
    
    for pattern in removal_patterns:
        text = re.sub(pattern, "", text, flags=re.IGNORECASE)
    
    return text.strip()


def extract_qa_pairs_from_text(content):
    # Adjusted regex pattern to match a broader variety of question and answer formats
    pattern = re.compile(r'(?:^|\.|\n)\s*([^\.]+?\?)([^\.]+?\.)', re.DOTALL)
    matches = pattern.findall(content)
    qa_pairs = [(preprocess_data(match[0]), preprocess_data(match[1])) for match in matches]
    return qa_pairs

def write_to_csv_with_preprocessing(qa_pairs, file_path, delimiter=','):
    with open(file_path, 'w', newline='', encoding='utf-8') as csvfile:
        csvwriter = csv.writer(csvfile, delimiter=delimiter)
        csvwriter.writerow(['Prompt', 'Response'])
        for question, answer in qa_pairs:
            csvwriter.writerow([question, answer])

def process_folder_to_single_csv(folder_path, output_csv_path, delimiter=','):
    all_qa_pairs = []
    for entry in os.scandir(folder_path):
        if entry.is_file() and entry.name.endswith('.txt'):
            input_txt_path = entry.path
            with open(input_txt_path, 'r', encoding='utf-8') as file:
                content = file.read()
            content = dynamic_remove_line_numbers(content)
            qa_pairs = extract_qa_pairs_from_text(content)
            all_qa_pairs.extend(qa_pairs)
            print(f"Processed {input_txt_path}")

    # Write all accumulated Q&A pairs to a single CSV file
    with open(output_csv_path, 'w', newline='', encoding='utf-8') as csvfile:
        csvwriter = csv.writer(csvfile, delimiter=delimiter)
        csvwriter.writerow(['Prompt', 'Response'])
        for question, answer in all_qa_pairs:
            csvwriter.writerow([question, answer])
    print(f"All Q&A pairs have been compiled into {output_csv_path}")


# Example usage
#folder_path = '/home/rami/crew_AI/100m-offers'
#output_csv_path = '/home/rami/crew_AI/text-output5.csv'
#process_folder_to_single_csv(folder_path, output_csv_path, delimiter=',')
    pass
