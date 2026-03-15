import anthropic
from dotenv import load_dotenv
import sys
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
    }
]

client = anthropic.Anthropic()

response = client.messages.create(model="claude-haiku-4-5-20251001",
                                  max_tokens=1024,
                                  tools=tools,
                                  messages=[
                                      {
                                      "role":"user",
                                      "content":"What is 347*23?"
                                     }])

if response.stop_reason == "tool_use":
    tool_block = response.content[0]
    tool_name = tool_block.name
    tool_input = tool_block.input
    
    if tool_name == "calculator":
        result = str(eval(tool_input["expression"]))
else:
    print("failed tool use")
    sys.exit()

followup = client.messages.create(model="claude-haiku-4-5-20251001",
                                  max_tokens=1024,
                                  tools=tools,
                                  messages=[
                                      {"role":"user", "content":"What is 347*23?"},
                                      {"role":"assistant", "content":response.content},
                                      {"role":"user",
                                       "content": [
                                           {"type":"tool_result",
                                            "tool_use_id": tool_block.id,
                                            "content":result
                                            }
                                       ]}
                                  ])

print(followup.content[0].text)
print(followup)