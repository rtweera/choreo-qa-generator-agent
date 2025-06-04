from app.app import run_app

runtime_config = {

}

if __name__=='__main__':
    # Use positive integer for number of questions and answers from each topic
    # use 0 to loop through topics and print them
    # use -1 to format the questions and answers into a JSONL file
    # use None to extract topics from the documentation
    run_app(-1)