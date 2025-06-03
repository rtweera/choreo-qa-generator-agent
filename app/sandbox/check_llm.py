import os
from langchain.chat_models import init_chat_model
from langchain_core.messages import HumanMessage, SystemMessage, AIMessage
from langchain_core.prompts import ChatPromptTemplate 
from dotenv import load_dotenv
from pprint import pprint

def read_doc(filepath: str) -> str:
    """Read the content of a file and return it as a string."""
    if not os.path.exists(filepath):
        raise FileNotFoundError(f"Current path is {os.getcwd()} and The file {filepath} does not exist.")
    with open(filepath, 'r', encoding='utf-8') as file:
        content = file.read()
    return content.strip()

def invoke():

    system_template = (
        "You are an AI assistant specialized in creating educational and technical questions. "
        "Given a specific topic from the Choreo documentation, generate a set of N diverse and "
        "insightful questions that assess understanding of the topic. The questions should vary "
        "in type (e.g., technical, non technical, practical etc.) and difficulty (basic to advanced)."
        "Ensure that each question is clear, concise, and directly related to the content provided."
        "The questions should be suitable for a range of audiences, from beginners to advanced users."
        "Don't mention about the Choreo documentation in the questions, just focus on the topic itself."
        "Ask questions like a user is facing these issues and trying to understand the topic better."
    )

    user_template = (
        "Topic: {topic_name}\n"
        "Documentation Excerpt: {documentation_excerpt}\n"
        "Documentation Content:\n"
        "{documentation_excerpt}\n\n"
        "Instructions:\n"
        "Based on the above documentation excerpt about '{topic_name}', generate {number_of_questions} "
        "questions that test comprehension and application of the material. The questions should:\n"
        "- Cover key concepts and details presented in the excerpt.\n"
        "- Vary in format (e.g., multiple-choice, true/false, short answer).\n"
        "- Range in difficulty from basic recall to higher-order thinking.\n\n"
        "Please provide the questions in a numbered list format.\n"
    )

    load_dotenv()
    if not os.getenv("GOOGLE_API_KEY"):
        raise Exception("Google API key not found")

    model = init_chat_model(
        model="gemini-2.5-flash-preview-04-17", model_provider="google_genai"
    )

    # print(model.invoke('Hello world'))
    prompt_template = ChatPromptTemplate.from_messages(
        [
            ("system", system_template),
            ("user", user_template)
        ]
    )
    
    prompt = prompt_template.invoke(
        {
            "topic_name": "Choreo Concepts",
            "documentation_excerpt": read_doc("./choreo-concepts.md"),
            "number_of_questions": 5
        }
    )

    response = model.invoke(prompt)
    if isinstance(response, AIMessage):
        pprint(response.model_dump())
        print("Response content:", response.content)
    else:
        raise Exception("Unexpected response type from model invocation")


if __name__ == "__main__":
    invoke()
