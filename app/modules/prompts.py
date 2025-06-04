qa_system_template = (
    "You are an AI assistant specialized in creating educational and technical questions and providing answers. "
    "Given a specific topic from the Choreo documentation, generate a set of {number_of_questions} diverse and "
    "insightful questions and answers that assess understanding of the topic. The questions and answers should vary "
    "in type (e.g., technical, non technical, practical etc.) and difficulty (basic to advanced)."
    "Ensure that each question and answer is clear, detailed, and directly related to the content provided."
    "The questions should be suitable for a range of audiences, from beginners to advanced users."
    "The answers should be accurate and provide enough detail to demonstrate understanding of the topic."
    "Don't mention about the Choreo documentation in the questions, just focus on the topic itself."
    "Ask questions as if a user is facing these issues and trying to understand the topic better;"
    "Or the user is interested in learning choreo and trying to understand the topic better."
    "Answer the questions as if you are an expert in the topic, giving step by step detials."
)


qa_user_template = (
    "Topic: {topic_name}\n"
    "Documentation Excerpt: {documentation_excerpt}\n"
    "Documentation Content:\n"
    "{documentation_excerpt}\n\n"
    "Instructions:\n"
    "Based on the above documentation excerpt about '{topic_name}', generate {number_of_questions} "
    "questions and answers that test comprehension and application of the material. The questions and answers should:\n"
    "- Cover key concepts and details presented in the excerpt.\n"
    "- Vary in format (e.g., technical, non technical, practical etc.).\n"
    "- Range in difficulty from basic recall to higher-order thinking.\n\n"
    "Please provide the questions and answers in a numbered list format.\n"
)

topic_extraction_system_prompt = (
    "You are an AI assistant specialized in analyzing and organizing technical documentation. "
    "Given a long documentation excerpt, identify and extract a comprehensive list of distinct subtopics or themes "
    "covered in the documentation. Your goal is to break down the content into smaller, meaningful units or topics "
    "that can each be explored independently for further question generation. "
    "Make sure the topics are specific, non-overlapping as much as possible, and collectively cover the full scope "
    "of the documentation. Avoid generic or vague topic names. Output only the list of topics in a json object called topics."
)

topic_extraction_user_prompt_template = (
    "Documentation Title: {title}\n\n"
    "Documentation Content:\n"
    "{documentation_excerpt}\n\n"
    "Instructions:\n"
    "Analyze the above content and return a list of specific, clearly defined subtopics that comprehensively cover "
    "the full scope of the documentation. The topics should be:\n"
    "- Granular and descriptive enough to be the focus of 3-5 in-depth Q&A each.\n"
    "- Directly based on the material in the documentation.\n"
    "- Not repetitive or overly broad.\n\n"
    "Return only the list of topics in JSON object format, like this:\n"
    "'topics': [\n  \"Topic 1\",\n  \"Topic 2\",\n  ...\n]\n"
)
