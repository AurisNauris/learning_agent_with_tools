import anthropic
from dotenv import load_dotenv
import sys
import time
load_dotenv()

tools = [
    {
        "name":"calculator",
        "description": "Evaluates a mathematical expression and returns the result. Use this for any math calculations.",
        "input_schema": {
            "type":"object",
            "properties": {
                "expression": {
                    "type":"string",
                    "description": "The math expression to evaluate, writen in latex style, e.g. '347*23'"
                }
            },
        "required": ["expression"]
        }
    },
    {
        "name":"get_weather",
        "description":"Gets the current temperature for a city in celcius.",
        "input_schema":{
            "type":"object",
            "properties":{
                "city":{"type":"string","description":"City name"}
            },
            "required":["city"]
        }
    }
]

client = anthropic.Anthropic()

i = 0
prompt = []

while True:

    user_input = input("You: ")
    if user_input.lower() in ["quit","exit"]:
        break
    prompt.append({"role":"user","content":user_input})

    while True:
        i += 1
        if i > 20: # to avoid accidental infinite loop for now
            break

        response = client.messages.create(model="claude-haiku-4-5-20251001",
                                        max_tokens=1024,
                                        tools=tools,
                                        messages=prompt)
        
        for block in response.content:
            if block.type == "text":
                print("Claude: ", block.text)

        if response.stop_reason == "end_turn":
            prompt.append({"role":"assistant",
                           "content":response.content})
            break

        if response.stop_reason == "tool_use":
            print("Tool used")
            tool_block = None
            for block in response.content:
                if block.type == "tool_use":
                    tool_block = block
                    break
            tool_name = tool_block.name
            tool_input = tool_block.input
            
            if tool_name == "calculator":
                result = str(eval(tool_input["expression"]))
                prompt.append({"role":"assistant", "content":response.content})
                prompt.append({"role":"user",
                            "content":[{
                                "type":"tool_result",
                                "tool_use_id":tool_block.id,
                                "content":result
                            }]})
            if tool_name == "get_weather":
                result = "22"
                prompt.append({"role":"assistant","content":response.content})
                prompt.append({"role":"user",
                            "content":[{
                                "type":"tool_result",
                                "tool_use_id": tool_block.id,
                                "content": result
                            }]})

        time.sleep(0.5)
