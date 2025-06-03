import os
from langchain.chat_models import init_chat_model
from langchain_core.messages import HumanMessage, SystemMessage, AIMessage
from dotenv import load_dotenv

def invoke():
    load_dotenv()
    if not os.getenv('GOOGLE_API_KEY'):
        raise Exception("Google API key not found")

    model = init_chat_model(model='gemini-2.0-flash', model_provider='google_genai')

    print(model.invoke('Give me a sample python code'))