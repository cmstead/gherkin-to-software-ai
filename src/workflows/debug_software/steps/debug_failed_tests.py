from src.utils.send_ai_query import send_query

from src.prompt_builder.construct_prompt import get_constructed_prompt
from src.prompt_types.prompt_type_constants import PROMPT_TYPES

def debug_failing_tests(prompt_values):
    prompt = get_constructed_prompt(PROMPT_TYPES["DEBUG_FAILED_TESTS"], prompt_values)
    
    response = send_query(prompt)
    
    return response.output_text