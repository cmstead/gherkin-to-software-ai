from src.prompt_types.gherkin_to_jest import PROMPT_FIELDS as GHERKIN_PROMPT_FIELDS, get_prompt as get_gherkin_prompt
from src.prompt_types.jest_to_software import PROMPT_FIELDS as JEST_PROMPT_FIELDS, get_prompt as get_jest_prompt
from src.prompt_types.debug_failed_tests import PROMPT_FIELDS as DEBUG_TEST_FIELDS, get_prompt as get_debug_prompt
from src.prompt_types.prompt_type_constants import PROMPT_TYPES

def get_constructed_prompt(prompt_type, prompt_values):
    prompt_fields = []
    prompt = ""
    
    if prompt_type == PROMPT_TYPES["DEBUG_FAILED_TESTS"]:
        prompt_fields = DEBUG_TEST_FIELDS
        prompt = get_debug_prompt()
    elif prompt_type == PROMPT_TYPES["GHERKIN_TO_JEST"]:
        prompt_fields = GHERKIN_PROMPT_FIELDS
        prompt = get_gherkin_prompt()
    elif prompt_type == PROMPT_TYPES["JEST_TO_SOFTWARE"]:
        prompt_fields = JEST_PROMPT_FIELDS
        prompt = get_jest_prompt()
    else:
        raise ValueError(f"Unknown prompt type: {prompt_type}")
    
    for field in prompt_fields:
        if field in prompt_values and prompt_values[field] is not None:
            prompt = prompt.replace(f"{{{field}}}", prompt_values[field])
        else:
            raise ValueError(f"Missing required field: {{{field}}}")

    return prompt