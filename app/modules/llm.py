import getpass
import os
from dotenv import load_dotenv
from langchain.chat_models import init_chat_model

from app.types.exceptions import APIKeyNotFoundError, InvalidModelProviderError
from app.constants import constants

load_dotenv(override=True, verbose=True)

class Llm:
    def __init__(self):
        self.model_provider = constants['model_provider']

        if self.model_provider == 'google':
            if not os.environ.get('GOOGLE_API_KEY'):
                raise APIKeyNotFoundError("GOOGLE_API_KEY")
            self.model = init_chat_model("gemini-2.0-flash", model_provider="google_genai")
            
        elif self.model_provider == 'openai':
            if not os.environ.get("OPENAI_API_KEY"):
                raise APIKeyNotFoundError("OPENAI_API_KEY") 
            self.model = init_chat_model("gpt-4o-mini", model_provider="openai")

        else:
            raise InvalidModelProviderError(self.model_provider)
        
        return self.model
    
    def invoke():
        ...