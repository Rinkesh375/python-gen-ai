from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()

client = OpenAI()

repsonse = client.chat.completions.create(
    model="gpt-4.1-mini",
    messages=[
        {
            "role": "user",
            "content": [
                {
                    "type": "text",
                    "text": "Generate a caption for this image in about 50 words"
                },
                {
                    "type": "image_url",
                    "image_url": {
                        "url": "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSblE2-_XcBg_bggULMwfNbXSMV89Y212nyFJ7a5GTO9w&s=10"
                    }
                }
            ]
        }
    ]
)


print("Response:", repsonse.choices[0].message.content)