import getpass
import os
from dotenv import load_dotenv
from langchain.chat_models import init_chat_model
from langchain_core.prompts import ChatPromptTemplate
from pathlib import Path
from langchain_core.output_parsers import PydanticOutputParser
from langchain_core.runnables import Runnable

from app.types.exceptions import APIKeyNotFoundError, InvalidModelProviderError
from app.constants import constants
from app.modules.prompts import qa_user_template, qa_system_template, topic_extraction_system_prompt, topic_extraction_user_prompt_template
from app.modules.utils import read_doc
from app.types.structured import TopicList


load_dotenv(override=True, verbose=True)

class Llm:
    def __init__(self):
        self.model = init_chat_model(
            model=constants['model'], 
            model_provider=constants['model_provider']
        )
        

    def invoke(self, system_template: str=qa_system_template, user_template: str=qa_user_template, topic_name: str=None, documentation_excerpt: Path=None, number_of_questions: int=None):
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
    
    def get_topics(self, system_template: str=topic_extraction_system_prompt, user_template: str=topic_extraction_user_prompt_template, documentation_excerpt: Path=None):
        prompt_template = ChatPromptTemplate.from_messages(
            [
                ("system", system_template),
                ("user", user_template)
            ]
        )

        parser = PydanticOutputParser(pydantic_object=TopicList)

        chain: Runnable = prompt_template | self.model | parser

        result = chain.invoke(
            {
                "documentation_excerpt": read_doc(documentation_excerpt),
                "title": documentation_excerpt.stem
            }
        )
        return "\n".join(result.topics)