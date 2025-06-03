import getpass
import os
from dotenv import load_dotenv
from langchain.chat_models import init_chat_model
from langchain_core.prompts import ChatPromptTemplate
from pathlib import Path

from app.types.exceptions import APIKeyNotFoundError, InvalidModelProviderError
from app.constants import constants
from app.modules.prompts import user_template, system_template, user_template_2, system_template_2
from app.modules.utils import read_doc

load_dotenv(override=True, verbose=True)

class Llm:
    def __init__(self):
        self.model = init_chat_model(
            model=constants['model'], 
            model_provider=constants['model_provider']
        )
        

    def invoke(self, system_template: str=system_template, user_template: str=user_template, topic_name: str=None, documentation_excerpt: Path=None, number_of_questions: int=5):
        prompt_template = ChatPromptTemplate.from_messages(
            [
                ("system", system_template),
                ("user", user_template)
            ]
        )
        prompt = prompt_template.invoke(
            {
                "topic_name": topic_name,
                "documentation_excerpt": read_doc(documentation_excerpt),
                "number_of_questions": number_of_questions
            }
        )

        response = self.model.invoke(prompt)
        return response.content, number_of_questions