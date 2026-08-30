from openai import OpenAI
from dotenv import load_dotenv
import json

load_dotenv()

client = OpenAI()


# ============================================================
# ALPACA-STYLE SYSTEM PROMPT
# ============================================================

SYSTEM_PROMPT = """
### Instruction:

You are an expert AI assistant that solves user queries in a structured way.

Follow these rules strictly:

1. First understand the user's request.
2. Start with a START step describing what the user wants.
3. Create a concise PLAN describing what needs to be done.
4. You may use multiple PLAN steps when necessary.
5. Only perform one step at a time.
6. Once the task is completely solved, return an OUTPUT step.
7. Do not expose private or detailed chain-of-thought reasoning.
8. PLAN content should contain only a concise summary of the reasoning/action being taken.
9. Always return valid JSON.
10. The JSON must contain exactly these two fields:

{
    "step": "START" | "PLAN" | "OUTPUT",
    "content": "string"
}

11. Do not add Markdown, explanations, or any text outside the JSON.
12. Follow this workflow:

START → PLAN → PLAN → ... → OUTPUT

Example:

User:
Solve 2 + 3 * 5 / 10

Assistant:
{
    "step": "START",
    "content": "The user wants to solve the mathematical expression 2 + 3 * 5 / 10."
}

Assistant:
{
    "step": "PLAN",
    "content": "Apply the order of operations, performing multiplication and division before addition."
}

Assistant:
{
    "step": "PLAN",
    "content": "Calculate 3 * 5 = 15, then calculate 15 / 10 = 1.5."
}

Assistant:
{
    "step": "OUTPUT",
    "content": "3.5"
}


### Input:

The user will provide a query that needs to be solved.

### Response:

Return exactly one JSON object using the required format.
"""


# ============================================================
# MESSAGE HISTORY
# ============================================================

message_history = [
    {
        "role": "system",
        "content": SYSTEM_PROMPT
    }
]


# ============================================================
# GET USER INPUT
# ============================================================

user_query = input("\nWrite your input: ")

message_history.append(
    {
        "role": "user",
        "content": user_query
    }
)


# ============================================================
# RUN AGENT
# ============================================================

while True:

    response = client.chat.completions.create(
        model="gpt-4o-mini",

        response_format={
            "type": "json_object"
        },

        messages=message_history
    )

    # --------------------------------------------------------
    # Get raw model response
    # --------------------------------------------------------

    raw_result = response.choices[0].message.content

    # --------------------------------------------------------
    # Save assistant response to conversation history
    # --------------------------------------------------------

    message_history.append(
        {
            "role": "assistant",
            "content": raw_result
        }
    )

    # --------------------------------------------------------
    # Parse JSON
    # --------------------------------------------------------

    try:
        parsed_result = json.loads(raw_result)

    except json.JSONDecodeError:
        print("\n❌ Invalid JSON returned by model:")
        print(raw_result)
        break

    # --------------------------------------------------------
    # Extract step and content
    # --------------------------------------------------------

    step = parsed_result.get("step")
    content = parsed_result.get("content")

    # ========================================================
    # START
    # ========================================================

    if step == "START":

        print("\n" + "=" * 60)
        print("👀 USER REQUEST")
        print("=" * 60)

        print(content)

    # ========================================================
    # PLAN
    # ========================================================

    elif step == "PLAN":

        print("\n🧠 PLAN")
        print("   └── " + content)

    # ========================================================
    # OUTPUT
    # ========================================================

    elif step == "OUTPUT":

        print("\n" + "=" * 60)
        print("🤖 FINAL ANSWER")
        print("=" * 60)

        print(content)

        print("=" * 60)

        break

    # ========================================================
    # UNKNOWN STEP
    # ========================================================

    else:

        print("\n❌ Unknown step returned by model:")
        print(parsed_result)

        break