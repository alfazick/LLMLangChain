
import sys
import os

# Add the root directory to the Python path
# Assuming your script is run from /workspaces/LLMLangChain/03Chains
sys.path.append('/workspaces/LLMLangChain')

from config_settings import API_KEY
from langchain_openai import OpenAI

# defining LLM model
llm = OpenAI(api_key=API_KEY,temperature=0.0)

from langchain.memory import ConversationBufferWindowMemory
from langchain.chains import ConversationChain

memory = ConversationBufferWindowMemory(k=1) # specifies number of messages to keep

memory.save_context(
    {"input":"Alex is an expert at sicilian defense."},
    {"output":"How can I assist you today?"})

memory.save_context(
    {"input": "Alex favorite opening is spanish variation"}, 
    {"output": "That's great to hear! "})

conversation = ConversationChain(
    llm = llm,
    memory = memory,
    verbose=True
)

print(conversation.invoke(input = "I am playing chess against Alex with black pieces. what to play, I need to win?"))

# k = 1

"""> Entering new ConversationChain chain...
Prompt after formatting:
The following is a friendly conversation between a human and an AI. The AI is talkative and provides lots of specific details from its context. If the AI does not know the answer to a question, it truthfully says it does not know.

Current conversation:
Human: Alex favorite opening is spanish variation
AI: That's great to hear! 
Human: I am playing chess against Alex with black pieces. what to play?
AI:

> Finished chain.
{'input': 'I am playing chess against Alex with black pieces. what to play?', 
'history': "Human: Alex favorite opening is spanish variation\nAI: That's great to hear! ", 
'response': " Well, based on Alex's favorite opening being the Spanish variation, 
I would suggest playing the Sicilian Defense as black. 
It is a popular and strong response to the Spanish opening. 
However, it ultimately depends on your own playing style and preferences. 
Do you have any specific openings or strategies that you prefer?"}

k = 2
> Entering new ConversationChain chain...
Prompt after formatting:
The following is a friendly conversation between a human and an AI. The AI is talkative and provides lots of specific details from its context. If the AI does not know the answer to a question, it truthfully says it does not know.

Current conversation:
Human: Alex is an expert at sicilian defense.
AI: How can I assist you today?
Human: Alex favorite opening is spanish variation
AI: That's great to hear! 
Human: I am playing chess against Alex with black pieces. what to play, I need to win?
AI:

> Finished chain.
{'input': 'I am playing chess against Alex with black pieces. what to play, I need to win?', 
'history': "Human: Alex is an expert at sicilian defense.\n
AI: How can I assist you today?\n
Human: Alex favorite opening is spanish variation\nAI: That's great to hear! ", 
'response': " Well, since Alex is an expert at Sicilian Defense, it might be a good idea 
to try a different opening. Have you considered the French Defense or the Caro-Kann Defense? 
These are both solid options against the Spanish Variation. 
However, it's important to remember that there is no guaranteed way to win in chess. 
It's all about strategy and adapting to your opponent's moves. Good luck!"}"""


# Note: you can pass 
# Alternately, we can also use ConversationTokenBufferMemory to store the recent interactions 
# by employing token length rather than the count of interactions. To do so, we can replace 
# memory = ConversationTokenBufferMemory(llm=llm, max_token_limit=100) to store the last 100 tokens 
# and import ConversationTokenBufferMemory