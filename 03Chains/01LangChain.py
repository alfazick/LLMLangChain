# basic entity is called LLM chain -> you ave one input and one output
# can be constructed ->User Query -> Chain: Prompt template + LLM + OutputParser(optional) -> Output


import sys
import os

# Add the root directory to the Python path
# Assuming your script is run from /workspaces/LLMLangChain/03Chains
sys.path.append('/workspaces/LLMLangChain')



from config_settings import API_KEY
from langchain_openai import OpenAI


# defining LLM model
llm = OpenAI(api_key=API_KEY,temperature=0.0)

from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain 

# creating the prompt template

prompt_template = PromptTemplate(
    input_variables=["book"],
    template="Name the author of the book {book}?",
)

# creating the chain 
chain = LLMChain(llm = llm,
                 prompt = prompt_template,
                 verbose = True)

# calling the chain

print(chain.invoke("The GodFather"))

# > Entering new LLMChain chain...
# Prompt after formatting:
# Name the author of the book The GodFather?

# > Finished chain.
# {'book': 'The GodFather', 'text': '\n\nMario Puzo'}