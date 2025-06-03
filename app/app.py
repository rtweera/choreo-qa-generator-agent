from app.constants import constants
from app.sandbox.check_llm import invoke
from app.modules.llm import Llm
import os

def run_app(constants=constants, runtime_cofig={}):
    llm = Llm()
    print(llm.invoke(
        topic_name="Choreo concepts",
        documentation_excerpt=os.path.join('output', 'concatenations', 'choreo-concepts.md'),
        number_of_questions=10
    ))
