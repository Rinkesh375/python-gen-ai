from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()

client = OpenAI()

# Few Shot Prompting: Directly giving the inst to the model and few examples to the model

SYSTEM_PROMPT = """
You should only and only answer the coding related questions. Do not ans anything else. Your name is Alexa. If user asks something other than coding, just say sorry.

Examples:

Q: Can you explain the a + b whole square?
A: Sorry, I can only help with Coding related questions.

Q: Hey, Write a code in python for adding two numbers.
A: def add(a, b):
       return a + b

"""

response = client.chat.completions.create(
    model="gpt-4o-mini",
   messages=[
    {"role": "system", "content": SYSTEM_PROMPT},
    {"role": "user", "content": "How to find prime number in programming"}
]
)


print(response.choices[0].message.content)