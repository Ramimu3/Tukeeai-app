import ebooklib
from ebooklib import epub
from bs4 import BeautifulSoup
import os


def extract_text_from_file(file_path):
    if file_path.lower().endswith('.pdf'):
        doc = fitz.open(file_path)
        text = ""
        for page in doc:
            text += page.get_text()
        num_pages = len(doc)
        doc.close()
        return text, True, num_pages  # Return text, is_pdf=True, and num_pages
    elif file_path.lower().endswith('.epub'):
        book = epub.read_epub(file_path)
        text = ""
        for item in book.get_items_of_type(ebooklib.ITEM_DOCUMENT):
            soup = BeautifulSoup(item.content, 'html.parser')
            text += soup.get_text()
        return text, False, 0  # Return text, is_pdf=False, and 0 for num_pages
    else:
        raise ValueError("Unsupported file format")



def extract_text_from_pdf(pdf_path):
    doc = fitz.open(pdf_path)
    text = ""
    for page in doc:
        text += page.get_text()
    doc.close()
    return text

def extract_text_from_epub(epub_path):
    book = epub.read_epub(epub_path)
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
    # Look for the nearest sentence end before the original end
    nearest_period = text.rfind('.', start, end)
    nearest_question = text.rfind('?', start, end)
    nearest_exclamation = text.rfind('!', start, end)
    new_end = max(nearest_period, nearest_question, nearest_exclamation) + 1
    # If there's no sentence-ending punctuation, just use the original end
    return new_end if new_end > start else end

def split_text_into_chunks(text, is_pdf=False, num_pages=0):
    if is_pdf and num_pages > 0:
        num_chunks = max(num_pages // 3, 1)  # At least 1 chunk if num_pages > 0
    else:
        # Assuming an average of 300 words per page, adjust this based on your needs
        avg_words_per_page = 300
        words = text.split()
        estimated_pages = len(words) // avg_words_per_page
        num_chunks = max(estimated_pages // 3, 1)  # Fall back to a heuristic for EPUBs

    total_length = len(text)
    chunk_size = total_length // num_chunks
    chunks = []
    start = 0
    for i in range(num_chunks):
        end = start + chunk_size
        if i < num_chunks - 1:  # Adjust end for all but the last chunk
            end = adjust_chunk_end(text, start, end)
        chunks.append(text[start:end])
        start = end  # Start the next chunk where the last one ended

    return chunks