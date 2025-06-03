from app.constants import constants
from app.sandbox.check_llm import invoke
from app.modules.llm import Llm
from app.modules.prompts import qa_user_template, qa_system_template, qa_user_template, qa_system_template
from app.modules.utils import write_to_file
import os

def run_app(n):
    llm = Llm()
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

