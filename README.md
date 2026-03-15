# learning_agent_with_tools
A simple project that helps to teach two things:
1. The use of tools with LLM API
2. The interactive and continuous chat

# Installation
1. Navigate on the terminal to the directory of choice
2. Create a new virtual environment
e.g. 
```
python -m venv vevn
```
3. Activate it
```
source venv/bin/activate
```
4. Install the required packages
```
pip install -r requirements.txt
```

# Usage
1. On the terminal run the code:
```
python main.py
```
2. Interact via command line by giving questions
3. Stop by typing "quit" or "exit"

# Short description
1. Two "tools" are defined to be used for the client
    a. "calculator" that uses your own python to execute the expression
    b. "get_weather" that gives always a temperature (used only b/c of demonstration purposes)
2. The while loop starts by prompting user to type the question
3. The inner while loop is entered where the question etc are passed to the model
    The "text" part of the response is printed
    a. Model may decide to use tools
    Response from this conversation are appended to the prompt to keep it continuous
    b. If tools were not needed, the response is appended to the prompt and the inner loop is exited.

# Obvious improvements
1. Security - no security checks in place - malicious prompts could do malicious things.
2. No checks on performance - the results may be totally off, the tools may be misused, etc.
3. The tools actually making more sense and connecting to the real services via api calls.

# Personal take 2026-03-15
1. It took some time to understand the use of tools.
    a. Initially it was quite confusing of how the tools such be written up as I never used the JSON schema before and how it will be related to the actual tool use etc. But looking it up and writing things up myself as well as changing some part of the descritpions and printing responses, it became clearer.
    b. I can now clearly see how the tool use can expand the capabilities of the LLM A LOT as well as making the results more realable (e.g. calculation of some expression is more reliable if done via python rather than LLM itself) as well as reduce the token usage.
    c. For the whole project I used only Haiku and it seemed to be very fast and reliable overall; however, for more complicated examples this may not be the case
2. It is fun to be able to build things that are actually useful quite quickly. It opens up ones eyes to see how many things are possible with not that much of expertise; like you don't need to study CS for years to be able to make really cool things (though I understand that those years spent on CS degree ensure that your products are much more reliable etc)
3. I would actually encourage a lot of people to get quick python fundamentals and then start building things themselves. Though not just copy/paste everything but also use LLM to ask how to write this part or that part and ask to explain things or watch then videos on specific parts or read forums. It is quite fun to be learning things on demand as well as because someone puts it on the schedule - I think I used to do more of the latter type - but a healthy mix of the two types of learning is probably the best.
4. It is somehow weird that some things only click after repeating them several times or by writing them out a few times. JSON Schema clicked only after I wrote several of them myself and realised it is simple; reading about it etc seemed more complicated. After repeating and writing a few of them myself made it more intuitive.