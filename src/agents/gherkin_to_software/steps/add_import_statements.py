from src.utils.send_ai_query import send_query

from src.prompt_builder.construct_prompt import get_constructed_prompt
from src.prompt_types.prompt_type_constants import PROMPT_TYPES

def add_import_statements(prompt_values):
    prompt = get_constructed_prompt(PROMPT_TYPES["ADD_IMPORT_STATEMENTS"], prompt_values)

    response = send_query(prompt)
    
    return response.output_text