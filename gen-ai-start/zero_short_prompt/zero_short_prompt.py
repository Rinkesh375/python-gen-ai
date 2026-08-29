from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()

client = OpenAI()

# Zero Shot Prompting: Directly giving the inst to the model
SYSTEM_PROMPT = "You should only and only answer the coding related questions. Do not ans anything else. Your name is Alex. If user asks something other than coding, just say sorry."

response = client.chat.completions.create(
    model="gpt-4o-mini",
   messages=[
    {"role": "system", "content": SYSTEM_PROMPT},
    {"role": "user", "content": "Hey, can you tell me a joke"}
]
)


print(response.choices[0].message.content)