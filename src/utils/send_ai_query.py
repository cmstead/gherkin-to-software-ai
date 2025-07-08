from dotenv import load_dotenv
from openai import OpenAI

from src.constants import AI_MODEL

load_dotenv()

client = OpenAI()

def send_query(prompt):
    return client.responses.create(
        model=AI_MODEL,
        input=prompt
    )