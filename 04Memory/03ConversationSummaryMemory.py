import sys
import os

# Add the root directory to the Python path
# Assuming your script is run from /workspaces/LLMLangChain/03Chains
sys.path.append('/workspaces/LLMLangChain')

from config_settings import API_KEY
from langchain_openai import OpenAI

# defining LLM model
llm = OpenAI(api_key=API_KEY,temperature=0.0)

from langchain.memory import ConversationSummaryMemory
from langchain.chains import ConversationChain

memory = ConversationSummaryMemory(llm=llm)

memory.save_context({"input": "Alex has a dog named Rocky."}, 
                    {"output": "Tell me more about Rocky!"})
memory.save_context({"input": "Alex also likes basketball"}, 
                    {"output": "Basketball is a great sport too!"})

conversation = ConversationChain(
    llm = llm,
    memory = memory,
    verbose = True 
)

print(conversation.invoke(input = "How old is Alex?"))
print(conversation.invoke(input = "What Alex likes to do?"))

# !!! Notice update in memory after the first question
"""> Entering new ConversationChain chain...
Prompt after formatting:
The following is a friendly conversation between a human and an AI. The AI is talkative and provides lots of specific details from its context. If the AI does not know the answer to a question, it truthfully says it does not know.

Current conversation:

The human mentions that Alex has a dog named Rocky and also likes basketball. The AI asks for more information about Rocky and comments that basketball is a great sport too.
Human: How old is Alex?
AI:

> Finished chain.
{'input': 'How old is Alex?', 
'history': '\nThe human mentions that Alex has a dog named Rocky and also likes basketball. 
The AI asks for more information about Rocky and comments that basketball is a great sport too.', 
'response': ' I do not have that information, but I do know that Alex has a dog named Rocky and enjoys playing basketball. Do you know anything else about Rocky? I am always interested in learning more about different animals.'}


> Entering new ConversationChain chain...
Prompt after formatting:
The following is a friendly conversation between a human and an AI. 
The AI is talkative and provides lots of specific details from its context. 
If the AI does not know the answer to a question, it truthfully says it does not know.

Current conversation:

The human mentions that Alex has a dog named Rocky and also likes basketball. 
The AI asks for more information about Rocky and comments that basketball is a great sport too. 
The human then asks about Alex's age, to which the AI responds that it does 
not have that information but is interested in learning more about Rocky.
Human: What Alex likes to do?
AI:

> Finished chain.
{'input': 'What Alex likes to do?', 'history': 
"\nThe human mentions that Alex has a dog named Rocky and also likes basketball. 
The AI asks for more information about Rocky and comments that basketball is a great sport too. 
The human then asks about Alex's age, to which the AI responds that it does not have that information 
but is interested in learning more about Rocky.", 
'response': ' Alex has a dog named Rocky and also enjoys playing basketball. 
Can you tell me more about Rocky? I am always interested in learning about different pets.'}"""