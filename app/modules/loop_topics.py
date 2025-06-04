from app.modules.utils import read_doc
from app.modules.llm import Llm
from pathlib import Path
from tqdm import tqdm

def loop_topics(topics_path:Path = None, llm:Llm = None, documentation_excerpt:Path = None, number_of_questions:int = None, system_template:str = None, user_template:str = None):
    """
    This function is used to loop through topics and perform operations on them.
    It is designed to be called in a loop, processing each topic in the list.
    """
    topics = read_doc(topics_path).splitlines()
    # For debugging purposes, print the topics
    if isinstance(number_of_questions, int) and number_of_questions <= 0:
        print(topics)    
        return
    total_n_questions = 0
    qa_bank: str = ""

    for topic in tqdm(topics, desc="Processing Topics", unit="topic"):
        result, n = llm.invoke(
            topic_name=topic,
            documentation_excerpt=documentation_excerpt,
            number_of_questions=number_of_questions,
            system_template=system_template,
            user_template=user_template
        )
        total_n_questions += n
        qa_bank += f"\n\n## {topic}\n\n{result}"
    
    return qa_bank, total_n_questions