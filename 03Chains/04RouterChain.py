import sys
import os

# Add the root directory to the Python path
# Assuming your script is run from /workspaces/LLMLangChain/03Chains
sys.path.append('/workspaces/LLMLangChain')



from config_settings import API_KEY
from langchain_openai import OpenAI


# defining LLM model
llm = OpenAI(api_key=API_KEY,temperature=0.0)

"""
Structure of the ==> Router Chain <==

The router chain consists of three key components:

Router chain: This chain decides the next chain to be called.

Destination chain: These chains represent the options available for the 
router chain to redirect the input to.

Default chain: When the router chain can’t decide which chain to use, 
it redirects to the default chain that provides a default output.
"""