import anthropic
from dotenv import load_dotenv
load_dotenv()

client = anthropic.Anthropic()

message = client.messages.create(model="claude-haiku-4-5-20251001",
                                 max_tokens=1024,
                                 messages=[{"role":"user", "content":"What should I search for to find the best advice about AI engineering roadmap?"}])


print(message.content)

