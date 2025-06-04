import re
import json
from pathlib import Path

def parse_section(section_content):
    """
    Parse a single section of markdown content to extract questions and answers.
    Returns a list of (question, answer) tuples.
    """
    qa_pairs = []
    # Match numbered questions and their answers
        # \d+\. matches one or more digits followed by a period, which typically indicates the start of a numbered question (e.g., "1.").
        # \s* allows for optional whitespace after the number and period.
        # \*\*Question:\*\* matches the literal string "Question:", which is likely used as a bolded label in Markdown.
        # \s* allows for optional whitespace after the "Question" label.
        # (.*?) is a non-greedy capture GROUP that matches the actual question text, capturing as little as 
        # possible up to the next part of the pattern.
        # \n\s*\*\*Answer:\*\* matches a newline, optional whitespace, and the literal "Answer:" label, again likely in Markdown.
        # \s* allows for optional whitespace after the "Answer" label.
        # (.*?) is another non-greedy capture GROUP that matches the answer text.
        # (?=(?:\d+\.\s*\*\*Question:\*\*|\Z)) is a lookahead that ensures the match ends right before the next question 
        # starts (another number and "Question:" label) or at the end of the string (\Z).
    pattern = r'(\d+\.\s*\*\*Question:\*\*\s*(.*?)\n\s*\*\*Answer:\*\*\s*(.*?)(?=(?:\d+\.\s*\*\*Question:\*\*|\Z)))'
    matches = re.finditer(pattern, section_content, re.DOTALL) # DOTALL makes it match across newlines too
    
    for match in matches:
        # group 1 is the full match, group 2 is the question text, group 3 is the answer text
        # groups are defined in the pattern by parentheses
        question = match.group(2).strip()   
        answer = match.group(3).strip()
        qa_pairs.append((question, answer))
    
    return qa_pairs

def extract_qa_to_structured_data(markdown_content):
    """
    Process markdown content, splitting by level-2 headers, and extract questions, answers, and topics.
    Returns a list of dictionaries with question, answer, and topic.
    """
    result = []
    # Split content by level-2 headers
    sections = re.split(r'^##\s*(.*?)\n', markdown_content, flags=re.MULTILINE) 
    # re.MULTILINE Changes the behavior of ^ and $ anchors so they match at the start and end of each line, not just the start and end of the whole string.
    # Sections are split into pairs: [header, content, header, content, ...]
    # Start from index 1 to skip any content before the first header
    # Example: re.split on '## a\nb\n##c\nd' -> ['', 'a', 'b\n', 'c', 'd']
    for i in range(1, len(sections), 2):
        topic = sections[i].strip()
        section_content = sections[i + 1].strip()
        try:
            qa_pairs = parse_section(section_content)
            for question, answer in qa_pairs:
                result.append({
                    'question': question,
                    'answer': answer,
                    'topic': topic
                })
        except Exception as e:
            print(f"Error parsing section '{topic}': {e}")
            continue  # Continue with the next section
    
    return result

def write_to_jsonl(data, output_file):
    """
    Write the extracted data to a JSONL file.
    """
    with open(output_file, 'w', encoding='utf-8') as f:
        for entry in data:
            f.write(json.dumps(entry) + '\n')

def format_qa(markdown_content: str, output_file: Path):
    structured_data = extract_qa_to_structured_data(markdown_content)
    # Write to JSONL
    write_to_jsonl(structured_data, output_file=output_file)
    
