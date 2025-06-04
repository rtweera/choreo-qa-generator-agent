from app.constants import constants
from app.sandbox.check_llm import invoke
from app.modules.llm import Llm
from app.modules.prompts import qa_user_template, qa_system_template, topic_extraction_system_prompt, topic_extraction_user_prompt_template
from app.modules.utils import write_to_file
from app.modules.loop_topics import loop_topics

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
    elif isinstance(n, int) and n>0:
        result, number_of_questions = loop_topics(
            topics_path=Path('output') / 'topics' / 'choreo-concepts' / 'topics-part-1.md',
            llm=llm,
            documentation_excerpt=Path('output') / 'concatenations' / 'choreo-concepts.md',
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
    elif isinstance(n, int) and n <= 0:
        topics_path = Path('output') / 'topics' / 'choreo-concepts' / 'topics-part-1.md'
        loop_topics(topics_path=topics_path)
    else:
        raise ValueError("Number of questions must be greater than 0 or None.")
