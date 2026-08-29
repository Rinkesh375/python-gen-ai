from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()

client = OpenAI()

response = client.chat.completions.create(
    model="gpt-4o-mini",
   messages=[
    {"role": "system", "content": "You are an expert in Maths and only and only as maths related"},
    {"role": "user", "content": "Hey, can you help me solve the a + b whole square"}
]
)


print(response)