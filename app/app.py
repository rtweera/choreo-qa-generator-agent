from app.constants import constants
from app.sandbox.check_llm import invoke
from app.modules.llm import Llm
from app.modules.prompts import qa_user_template, qa_system_template, topic_extraction_system_prompt, topic_extraction_user_prompt_template
from app.modules.utils import write_to_file, read_doc
from app.modules.loop_topics import loop_topics
from app.modules.format_qa import format_qa

import os
from pathlib import Path

def run_app(n: int = None):
    llm = Llm()
    # Extract topics from the documentation if n is None
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
    # If n is a positive integer, generate questions and answers
    elif isinstance(n, int) and n>0:
        result, number_of_questions = loop_topics(
            topics_path=Path('output') / 'topics' / 'choreo-concepts' / 'topics-part-2.md',
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
    # If n is 0, loop through topics and print them
    elif isinstance(n, int) and n == 0:
        topics_path = Path('output') / 'topics' / 'choreo-concepts' / 'topics-part-2.md'
        loop_topics(topics_path=topics_path)
    # If n is -1, format the questions and answers into a JSONL file
    elif isinstance(n, int) and n == -1:
        format_qa(
            markdown_content=read_doc(Path('output') / 'questions-and-answers' / 'choreo-concepts' / 'q-and-a-together-part-14-76qty.md'),
            output_file=Path('output') / 'formatted-questions-and-answers' / 'choreo-concepts' / 'fmt-q-and-a-together-part-14-76qty.jsonl'
        )
    else:
        raise ValueError("Number of questions must be greater than 0 or None.")
