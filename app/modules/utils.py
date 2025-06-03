from pathlib import Path
import os
import json

def read_doc(filepath: str) -> str:
    """Read the content of a file and return it as a string."""
    if not os.path.exists(filepath):
        raise FileNotFoundError(f"Current path is {os.getcwd()} and The file {filepath} does not exist.")
    with open(filepath, 'r', encoding='utf-8') as file:
        content = file.read()
    return content.strip()


def write_to_file(directory: Path, content: str, number_of_questions: int):
    """
    Writes the given content to a file at the specified path.
    
    :param directory: Path to the file where content should be written.
    :param content: Content to write into the file.
    """

    # extract the directory from the file path
    index_path = os.path.join(directory, 'index.json')

    # Default index content
    index_content = {
        "i": 1,
        "filename_prefix": 'file'
    }

    with open(index_path, 'r', encoding='utf-8') as index_file:
        try:
            index_content = json.load(index_file)
            # increment the index value
            index_content['i'] += 1
            index_content['filename_prefix'] = index_content.get('filename_prefix', 'file')
        except json.JSONDecodeError:
            raise ValueError(f"Invalid JSON in index file: {index_path}. Please check the file content.")
        
    with open(os.path.join(directory, 'index.json'), 'w', encoding='utf-8') as index_file:
        # write the updated index content back to the index file    
        json.dump(index_content, index_file, indent=4)

    file_path = os.path.join(directory, f"{index_content['filename_prefix']}-part-{index_content['i']}-{number_of_questions}qty.md")

    with open(file_path, 'w', encoding='utf-8') as file:
        file.write(content)