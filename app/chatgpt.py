from openai import OpenAI
import os
from dotenv import load_dotenv

load_dotenv()
client = OpenAI()
client.api_key = "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"
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
