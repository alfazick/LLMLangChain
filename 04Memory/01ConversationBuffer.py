"""
1.Upon receiving a user query, a chain combined with conversations in the memory then passes to the model.

2. After the chain generates a response, it is subsequently stored in the memory, ensuring that the context 
and information derived from this interaction are preserved for future use.


A conversation buffer is the most basic and simple type of memory that keeps 
track of the conversations between the AI and the user. This buffer serves as input or context for generating responses. 
The model considers the context of the ongoing conversation, making responses more coherent and relevant.
"""

import sys
import os

# Add the root directory to the Python path
# Assuming your script is run from /workspaces/LLMLangChain/03Chains
sys.path.append('/workspaces/LLMLangChain')

from config_settings import API_KEY
from langchain_openai import OpenAI

# defining LLM model
llm = OpenAI(api_key=API_KEY,temperature=0.0)

from langchain.memory import ConversationBufferMemory
from langchain.chains import ConversationChain


memory = ConversationBufferMemory()

memory.save_context(
    {"input":"Alex is an avid chess player."},
    {"output":"Hello Alex! How can I assist you today?"})

memory.save_context(
    {"input": "Alex favorite opening is spanish variation"}, 
    {"output": "That's great to hear! "})

conversation = ConversationChain(
    llm = llm,
    memory = memory,
    verbose=True
)

print(conversation.invoke(input = "I am playing chess against Alex with black pieces. what to play?"))

"""
> Entering new ConversationChain chain...
Prompt after formatting:
The following is a friendly conversation between a human and an AI. The AI is talkative and provides lots of specific details from its context. If the AI does not know the answer to a question, it truthfully says it does not know.

Current conversation:
Human: Alex is an avid chess player.
AI: Hello Alex! How can I assist you today?
Human: Alex favorite opening is spanish variation
AI: That's great to hear! 
Human: I am playing chess against Alex with black pieces. what to play?
AI:

> Finished chain.
{'input': 'I am playing chess against Alex with black pieces. what to play?', 
'history': "Human: Alex is an avid chess player.\n
AI: Hello Alex! How can I assist you today?\nHuman: 
Alex favorite opening is spanish variation\nAI: That's great to hear! ", 

'response': " Well, based on Alex's favorite opening being the Spanish variation, 
I would suggest playing the Sicilian Defense as black. 
It is a popular and effective response to the Spanish opening. 
However, it ultimately depends on your own playing style and strategy. 
Do you have any other preferences or specific questions about the game?"}
"""