from openai import OpenAI
from dotenv import load_dotenv
import json
import requests
from urllib.parse import quote
from pydantic import BaseModel, Field
from typing import Optional

# --------------------------------------------------
# 1. SETUP
# --------------------------------------------------

load_dotenv()

client = OpenAI()


# --------------------------------------------------
# 2. TOOLS
# --------------------------------------------------

def get_weather(city: str):
    """
    Get current weather information for a city.
    """

    city = city.strip()

    if not city:
        return "City name cannot be empty."

    url = f"https://wttr.in/{quote(city)}?format=%C+%t"

    try:
        response = requests.get(url, timeout=10)

        if response.status_code == 200:
            return f"The weather in {city.title()} is {response.text.strip()}"

        return f"Could not get weather for {city}."

    except requests.RequestException as error:
        return f"Weather service failed: {error}"


# All tools available to our AI agent
available_tools = {
    "get_weather": get_weather
}


# --------------------------------------------------
# 3. SYSTEM PROMPT
# --------------------------------------------------

SYSTEM_PROMPT = """
You are an AI Agent that solves user queries step-by-step.

You have four types of steps:

1. START
   - Represents the user's request.

2. PLAN
   - Decide what needs to be done.
   - You may have multiple PLAN steps.

3. TOOL
   - Use a tool when external information is required.
   - After calling a tool, wait for the OBSERVE step.

4. OUTPUT
   - Give the final answer to the user.
   - OUTPUT must only happen when you have enough information.

Rules:

- Return ONLY valid JSON.
- Execute only ONE step at a time.
- Do not directly answer before completing the required steps.
- If a tool is required, use the available tool.
- After TOOL, wait for OBSERVE.
- After OBSERVE, continue planning if necessary.
- Finally return OUTPUT.
- Keep PLAN messages short and simple.

Available tools:

get_weather(city: str)
- Takes a city name.
- Returns the current weather information.

JSON format:

START:
{
    "step": "START",
    "content": "string"
}

PLAN:
{
    "step": "PLAN",
    "content": "string"
}

TOOL:
{
    "step": "TOOL",
    "tool": "get_weather",
    "input": "city name"
}

OBSERVE:
{
    "step": "OBSERVE",
    "tool": "get_weather",
    "input": "city name",
    "output": "tool result"
}

OUTPUT:
{
    "step": "OUTPUT",
    "content": "final answer"
}


Example:

User:
What is the weather in Delhi?

Assistant:
{
    "step": "START",
    "content": "User wants the current weather in Delhi."
}

Assistant:
{
    "step": "PLAN",
    "content": "I need to get the current weather for Delhi."
}

Assistant:
{
    "step": "TOOL",
    "tool": "get_weather",
    "input": "Delhi"
}

After receiving the tool result:

Assistant:
{
    "step": "PLAN",
    "content": "I now have the weather information for Delhi."
}

Assistant:
{
    "step": "OUTPUT",
    "content": "The current weather in Delhi is cloudy and 20°C."
}
"""


class MyOutputFormat(BaseModel):
    step: str = Field(..., description="The ID of the step. Example: PLAN, OUTPUT, TOOL, etc")
    content: Optional[str] = Field(None, description="The optional string content for the step")
    tool: Optional[str] = Field(None, description="The ID of the tool to call.")
    input: Optional[str] = Field(None, description="The input params for the tool")

# --------------------------------------------------
# 4. MESSAGE HISTORY
# --------------------------------------------------

message_history = [
    {
        "role": "system",
        "content": SYSTEM_PROMPT
    }
]

while True:

    # --------------------------------------------------
    # 5. GET USER INPUT
    # --------------------------------------------------

    user_query = input("\n👤 You: ").strip()

    message_history.append({
        "role": "user",
        "content": user_query
    })


    # --------------------------------------------------
    # 6. AGENT LOOP
    # --------------------------------------------------

    while True:

        # Ask the AI what the next step should be
        response = client.chat.completions.parse(
            model="gpt-4o-mini",
            response_format=MyOutputFormat,
            messages=message_history
        )

        # Get AI response
        raw_result = response.choices[0].message.conent

        # Save AI response in conversation history
        message_history.append({
            "role": "assistant",
            "content": raw_result
        })
        
        parsed_result = response.choices[0].message.parsed



        # --------------------------------------------------
        # 7. READ AI STEP
        # --------------------------------------------------

        step = parsed_result.step
        content = parsed_result.content


        # --------------------------------------------------
        # START
        # --------------------------------------------------

        if step == "START":

            print("\n" + "=" * 60)
            print("👀 USER REQUEST")
            print("=" * 60)

            print(content)


        # --------------------------------------------------
        # PLAN
        # --------------------------------------------------

        elif step == "PLAN":

            print("\n🧠 PLAN")
            print(f"   └── {content}")


        # --------------------------------------------------
        # TOOL
        # --------------------------------------------------

        elif step == "TOOL":

            tool_name = parsed_result.tool
            tool_input = parsed_result.input

            print("\n🔧 TOOL CALL")
            print(f"   Tool  : {tool_name}")
            print(f"   Input : {tool_input}")


            # Check whether tool exists
            if tool_name not in available_tools:

                tool_response = f"Tool '{tool_name}' does not exist."

            else:

                try:

                    # Get actual Python function
                    tool_function = available_tools[tool_name]

                    # Execute function
                    tool_response = tool_function(tool_input)

                except Exception as error:

                    tool_response = f"Tool execution failed: {error}"


            # --------------------------------------------------
            # OBSERVE
            # --------------------------------------------------

            print("\n🔍 OBSERVE")
            print(f"   └── {tool_response}")


            # Send tool result back to AI
            observe_message = {
                "step": "OBSERVE",
                "tool": tool_name,
                "input": tool_input,
                "output": tool_response
            }

            message_history.append({
                "role": "developer",
                "content": json.dumps(observe_message)
            })


        # --------------------------------------------------
        # OUTPUT
        # --------------------------------------------------

        elif step == "OUTPUT":

            print("\n" + "=" * 60)
            print("🤖 FINAL ANSWER")
            print("=" * 60)

            print(content)

            print("=" * 60)

            break


        # --------------------------------------------------
        # UNKNOWN STEP
        # --------------------------------------------------

        else:

            print(f"\n❌ Unknown step received: {step}")
            print(parsed_result)

            break