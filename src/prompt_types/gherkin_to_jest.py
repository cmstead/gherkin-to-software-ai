from src.utils.fs import read_file

PROMPT_FIELDS = [
    "Persona",
    "Gherkin"
]

def get_prompt():
    return read_file("ai_files/prompts/gherkin-to-jest.md")