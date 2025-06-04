from app.constants import constants
from app.sandbox.check_llm import invoke
from app.modules.llm import Llm
from app.modules.prompts import qa_user_template, qa_system_template, topic_extraction_system_prompt, topic_extraction_user_prompt_template
from app.modules.utils import write_to_file
import os
from pathlib import Path

def run_app(n: int = None):
    llm = Llm()
    if n is None:
        result = llm.get_topics(
            system_template=topic_extraction_system_prompt,
            user_template=topic_extraction_user_prompt_template,
            documentation_excerpt=Path('output') / 'concatenations' / 'choreo-concepts.md'
        )
        write_to_file(
            directory=Path('output') / 'topics' / 'choreo-concepts',
            content=result,
            number_of_questions=None
        )
        print(f"Extracted Topics:\n{result}")
        return
    elif n is int and n>0:
        result, number_of_questions = llm.invoke(
            topic_name="Choreo concepts",
            documentation_excerpt=os.path.join('output', 'concatenations', 'choreo-concepts.md'),
            number_of_questions=n,
            system_template=qa_system_template,
            user_template=qa_user_template
        )
        write_to_file(
            directory=os.path.join('output', 'questions-and-answers', 'choreo-concepts'),
            content=result,
            number_of_questions=number_of_questions
        )
        print(f"Generated Questions:\n{result}")
    else:
        raise ValueError("Number of questions must be greater than 0 or None.")
