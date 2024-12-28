from openai import OpenAI
import os
from dotenv import load_dotenv

load_dotenv()
client = OpenAI()
client.api_key = os.getenv('OPENAI_API_KEY')
def ask_chatgpt(prompt: str) -> str:

    print('KEYOPEN',client.api_key)
    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "user", "content": prompt}
        ],
        temperature=0.7
    )
    response_message = response.choices[0].message.content
    return response_message
