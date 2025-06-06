# Choreo QA Generator Agent

This project is a Question & Answer (QA) generation tool designed to process Choreo documentation and automatically generate educational and technical questions and answers. It is intended to help developers, educators, and documentation writers quickly create structured Q&A datasets from Markdown documentation.

## Project Structure

- **main.py**: Entry point for running the application.
- **requirements.txt**: Lists Python dependencies for the project.
- **app/**: Main application package.
  - **app.py**: Main application logic or runner script.
  - **constants.py**: Stores constant values used throughout the app (e.g., model names, providers).
  - **modules/**: Contains core modules for processing and formatting.
    - **llm.py**: Handles interactions with language models (LLMs) for generating questions, answers, and extracting topics.
    - **format_qa.py**: Parses and formats markdown Q&A content into structured data (e.g., JSONL).
    - **format_concat.py**: Likely used for concatenating or merging formatted outputs.
    - **loop_topics.py**: Automates looping over topics to generate or process Q&A for each topic.
    - **prompts.py**: Stores prompt templates for LLM interactions.
    - **utils.py**: Utility functions (e.g., file reading, helpers).
  - **sandbox/**: Experimental and test scripts.
    - **check_llm.py**: Script to test LLM calls and prompt templates.
    - **simple_llm.py**: Minimal example for LLM usage.
    - **choreo-concepts.md**: Example documentation file for testing.
  - **types/**: Custom types and exceptions.
    - **exceptions.py**: Custom exception classes (e.g., for missing API keys).
    - **structured.py**: Pydantic models for structured data parsing and validation.
- **choreo-docs/**: Contains documentation projects (e.g., for MkDocs).
  - **developer-docs/**: Developer documentation with its own `mkdocs.yml` and docs folder.
  - **pe-docs/**: Platform Engineer documentation set (structure similar to developer-docs).
- **output/**: Stores generated outputs.
  - **concatenations/**, **formatted-questions-and-answers/**, **hierarchy/**, **questions-and-answers/**, **summaries/**, **topics/**: Organized output folders for different types of generated data.
- **logs/**: Log files generated by the application.
- **todo/**: Contains project TODOs and planning notes.

## How It Works

1. **Documentation Parsing**: The tool reads Markdown documentation files (e.g., from `choreo-docs/`).
2. **Topic Extraction**: Uses LLMs to extract topics from documentation sections.
3. **Q&A Generation**: For each topic, the LLM generates a set of questions and answers, which are then parsed and structured.
4. **Formatting**: The Q&A pairs are formatted and saved as JSONL or other structured formats for downstream use.
5. **Output Organization**: Results are saved in the `output/` directory, organized by type and topic.

## Key Components

- **LLM Integration**: Uses LangChain and various LLM providers (e.g., Google Gemini) for question generation and topic extraction.
- **Prompt Engineering**: Customizable prompt templates for different tasks (in `prompts.py`).
- **Structured Parsing**: Regex and Pydantic models are used to parse and validate the generated Q&A content.
- **Error Handling**: Custom exceptions for missing API keys and invalid model configurations.

## Getting Started

1. **Install dependencies**:
   ```sh
   pip install -r requirements.txt
   ```
2. **Set up environment variables** (e.g., API keys for LLM providers).
3. **Run the main script**:
   ```sh
   python main.py
   ```
4. **Check outputs** in the `output/` directory.

## Developer Notes

- **Modular Design**: Each module in `app/modules/` is responsible for a specific part of the pipeline.
- **Sandboxing**: Use `app/sandbox/` for testing new prompts, LLMs, or data formats.
- **Documentation**: The `choreo-docs/` folder contains MkDocs-based documentation for Choreo itself, which can be used as input for the QA generator.

## Contributing

Feel free to open issues or submit pull requests to improve the tool, add new features, or fix bugs.

---

This README provides a high-level overview. For more details, review the code in each module and the example scripts in `app/sandbox/`.