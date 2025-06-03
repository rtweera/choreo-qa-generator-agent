import os

def read_doc(filepath: str) -> str:
    """Read the content of a file and return it as a string."""
    if not os.path.exists(filepath):
        raise FileNotFoundError(f"Current path is {os.getcwd()} and The file {filepath} does not exist.")
    with open(filepath, 'r', encoding='utf-8') as file:
        content = file.read()
    return content.strip()
