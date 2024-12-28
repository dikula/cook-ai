import base64
import openai
# client = OpenAI()

# Function to encode the image
def encode_image(image_path):
    with open(image_path, "rb") as image_file:
        return base64.b64encode(image_file.read()).decode("utf-8")


# Path to your image
image_path = "/Users/urosfww/workspace/cook_ai/app/frizider.png"
openai.api_key = "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"
# Getting the base64 string
base64_image = encode_image(image_path)

response = openai.ChatCompletion.create(
    model="gpt-4o-mini",
    messages=[
        {
            "role": "user",
            "content": [
                {
                    "type": "text",
                    "text": "What is in this image?",
                },
                {
                    "type": "image_url",
                    "image_url": {"url": f"data:image/jpeg;base64,{base64_image}"},
                },
            ],
        }
    ],
)

print(response.choices[0])