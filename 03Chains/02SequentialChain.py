

# we can combine multiple chains together chain1 -> chain2 -> chainN -> output 
# it's basically pipeline of chains

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
from langchain.chains import SimpleSequentialChain

prompt_1 = PromptTemplate(
    input_variables=["book"],
    template="Name the author who wrote the book {book}"
)
chain_1 = LLMChain(llm=llm,prompt=prompt_1)

prompt_2 = PromptTemplate(
    input_variables=["author_name"],
    template="Write a 50-word biography for the following author:{author_name}"
)
chain_2 = LLMChain(llm=llm, prompt = prompt_2)

# Combine into simple sequential chain 
simple_sequential_chain = SimpleSequentialChain(chains = [chain_1,chain_2],verbose=True)

# run the chain
simple_sequential_chain.invoke("The GodFather")

# > Entering new SimpleSequentialChain chain...


# Mario Puzo


# Mario Puzo was an Italian-American author best known for his novel "The Godfather," 
# which was adapted into a highly successful film trilogy. He was born in New York City in 1920 and 
# began his writing career as a freelance writer for magazines. 
# Puzo's works often explored themes of power, family, and the American Dream.

# > Finished chain.