import os
from crewai import Agent, Task, Crew, Process
from langchain_community.llms import Ollama
from textwrap import dedent
from langchain_openai import ChatOpenAI
from concurrent.futures import ProcessPoolExecutor 
from langchain.agents import Tool
from langchain_community.llms import HuggingFaceEndpoint

#llm_openai = ChatOpenAI(
 #  openai_api_key="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",
  #model_name="gpt-3.5-turbo-0125",  # Specified model
   #openai_api_base="https://api.openai.com/v1"  # OpenAI API endpoint
#)
llm = HuggingFaceEndpoint(
endpoint_url="https://api-inference.huggingface.co/models/mistralai/Mixtral-8x7B-Instruct-v0.1",
huggingfacehub_api_token="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",
task="text-generation"
)

#llm_lmstudio = ChatOpenAI(
 #  openai_api_base="http://localhost:1234/v1",
  # openai_api_key="no-key",
   #model_name=""
#)
llm_ollama=Ollama(model="mistralpara8q")

class QuestionGenerationCrew:
    def __init__(self, text_segments, num_questions=30, num_answers=30, num_pair=30):
        self.text_segments = text_segments
        self.num_questions = num_questions
        self.num_answers = num_answers
        self.num_pair = num_pair


    def create_agents(self):
        # Employees/Experts
        question_generator = Agent(
            role='Question Generator',
            goal=f'Generate at least {self.num_questions} insightful questions about the text.',
            backstory='This agent specializes in critical thinking and question formation. It leverages the segmented text to craft questions that probe deeper into the content, facilitating understanding and engagement.',
            verbose=True,
            allow_delegation=False,
            llm=llm,
        )

        question_writer_and_answer_provider = Agent(
        role='Question Writer and Answer Provider',
        goal=f'Write down the generated questions and provide at least {self.num_answers} detailed, expansive answers to these questions, combining them into a {self.num_pair} coherent question-answer format without changing the original question.',
        backstory='An adept content creator and analyst, this agent excels at interpreting and responding to complex questions with comprehensive, insightful answers. With a strong background in content synthesis, it ensures each question is addressed thoroughly, facilitating a deep engagement with the content.',
        verbose=True,
        memory=True,
        allow_delegation=False,
        llm=llm,
    )
    

        return question_generator, question_writer_and_answer_provider

    def create_task(self, task_name, agent, task_summary, detailed_description, parameters, note, context=None):
     if task_name == "GenerateQuestions":
        expected_output = f"A list of at least {self.num_questions} insightful questions."
     elif task_name == "OrganizeAndIntegrate":
        expected_output=f"At least {self.num_pair} coherent pairs of questions and answers, clearly labeled and integrated without changing the original text."
     
     description = dedent(f"""
    **Task**: {task_summary}
    **Description**: {detailed_description}
    **Parameters**:
    """) + '\n'.join([f"- {param}: {desc}" for param, desc in parameters.items()]) + dedent(f"""
    **Note**: {note}
    **Expected Output**: {expected_output}
    """)
     return Task(description=description, agent=agent, expected_output=expected_output)


    def generate_tasks(self, question_generator, question_writer_and_answer_provider ):
     tasks = []
     for segment in self.text_segments:

        # Generation of questions task
        question_task = self.create_task(
            task_name="GenerateQuestions",
            agent=question_generator,
            task_summary="Create a list of questions based on the text, without using any external tools.",
            detailed_description=f"Use the text segments to generate an insightful list of questions that facilitate understanding and engagement with the content. Text segment: '{segment}'",
            parameters={"Number of Questions": f"Generate at least {self.num_questions} questions."},
            note="Focus on crafting questions that probe deeper into the content."
        )
        tasks.append(question_task)

        # Combined task for organizing and integrating text with questions
        organize_and_integrate_task = self.create_task(
            task_name="OrganizeAndIntegrate",
            agent=question_writer_and_answer_provider,  # Assuming this agent now handles both organizing and integrating
            task_summary="Answer the questions and integrate with the original text.",
            detailed_description=f"Based on the generated questions, answer them using the original text segment: '{segment}'. Then, integrate these answers with the questions to form coherent pairs.",
            parameters={
                "Number of Questions": f"answer at least {self.num_questions} questions.",
                "Number of Pairs": f"Generate at least {self.num_pair} unique pairs of questions and answers."
            },
            note="Ensure the answers are detailed, using direct quotes from the text where applicable. Maintain clarity and coherence throughout.",
        )
        tasks.append(organize_and_integrate_task)

     return tasks
    
    def process_segment(question_generator, question_writer_and_answer_provider, segment):
      questions = question_generator.process(segment)  # Question Generation
      qa_pairs = question_writer_and_answer_provider.process(segment, questions)  # Answering and Integration
      return qa_pairs


    
    def export_to_file(self, filename, result):
     """
    Exports the result to a text file.
    
    :param filename: The name of the file to export the result to.
    :param result: The result string to be written to the file.
    """
     with open(filename, 'w', encoding='utf-8') as file:
        file.write(result)




    def run(self, base_name):
     question_generator, question_writer_and_answer_provider  = self.create_agents()
     tasks = self.generate_tasks(question_generator, question_writer_and_answer_provider )
    
     question_generation_crew = Crew(
        agents=[question_generator, question_writer_and_answer_provider],
        tasks=tasks,
        process=Process.sequential,  # Ensuring a hierarchical process.
        verbose=2,
    )

     result = question_generation_crew.kickoff()
    # Include the base name in the output file's name
     self.export_to_file(f"{base_name}_output.txt", result)

     return result


def read_text_file(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        text = file.read()
    segments = [text]  # Treat the entire text as a single segment; adjust if necessary
    return segments

def process_file(file_path, user_id):
    # User-specific directory for saving output
    user_specific_dir = os.path.join(os.path.dirname(file_path), f"user_{user_id}")
    os.makedirs(user_specific_dir, exist_ok=True)  # Ensure the directory exists
    
    # Adjust base_name to include user-specific directory
    base_name = os.path.join(user_specific_dir, os.path.splitext(os.path.basename(file_path))[0])
    
    # Proceed with processing as before
    text_segments = read_text_file(file_path)
    question_generation_crew = QuestionGenerationCrew(text_segments)
    results = question_generation_crew.run(base_name)
    
    return results



def process_folder(folder_path, user_id):
    file_paths = [os.path.join(folder_path, filename) for filename in os.listdir(folder_path) if os.path.isfile(os.path.join(folder_path, filename))]
    
    # Adjust executor mapping to include user_id
    with ProcessPoolExecutor(max_workers=3) as executor:
        results = list(executor.map(process_file, file_paths, [user_id] * len(file_paths)))
    
    # Results processing remains as needed


    # Here, results will be a list of the results from processing each file.
    # You can further process or aggregate these results as needed.

if __name__ == "__main__":
    print("## Welcome to the Question Generation Crew")
    print('-------------------------------------------')
    folder_path = '/home/rami/crew_AI/chunks'  # Set to your specific folder path
    user_id = "1"  # Set to your specific user ID
    process_folder(folder_path, user_id)
