import anthropic
from dotenv import load_dotenv

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

