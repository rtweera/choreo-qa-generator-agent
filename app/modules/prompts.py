system_template = (
    "You are an AI assistant specialized in creating educational and technical questions. "
    "Given a specific topic from the Choreo documentation, generate a set of N diverse and "
    "insightful questions that assess understanding of the topic. The questions should vary "
    "in type (e.g., technical, non technical, practical etc.) and difficulty (basic to advanced)."
    "Ensure that each question is clear, concise, and directly related to the content provided."
    "The questions should be suitable for a range of audiences, from beginners to advanced users."
    "Don't mention about the Choreo documentation in the questions, just focus on the topic itself."
    "Ask questions as if a user is facing these issues and trying to understand the topic better;"
    "Or the user is interested in learning choreo and trying to understand the topic better."
)

user_template = (
    "Topic: {topic_name}\n"
    "Documentation Excerpt: {documentation_excerpt}\n"
    "Documentation Content:\n"
    "{documentation_excerpt}\n\n"
    "Instructions:\n"
    "Based on the above documentation excerpt about '{topic_name}', generate {number_of_questions} "
    "questions that test comprehension and application of the material. The questions should:\n"
    "- Cover key concepts and details presented in the excerpt.\n"
    "- Vary in format (e.g., multiple-choice, true/false, short answer).\n"
    "- Range in difficulty from basic recall to higher-order thinking.\n\n"
    "Please provide the questions in a numbered list format.\n"
)