# This will represent the debug workflow
# For now it will need the following items:
# - tests to run
# - failing code
# - debug output

# This will follow the same flow as the gherkin to software flow
# where the debug steps will run multiple times
# until either the tests pass or the number of tries is exceeded

from src.workflows.debug_software.steps.debug_failed_tests import debug_failing_tests
from src.utils.run_tests import run_tests
from src.utils.send_ai_query import send_query