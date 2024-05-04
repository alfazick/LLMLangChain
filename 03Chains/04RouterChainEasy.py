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

# Case Study: Library FAQ Chatbot
"""
+-------------------+
|    User Query     |
+-------------------+
          |
          v
+-------------------+
|   Router Chain    |
| (LLMRouterChain)  |
+-------------------+
          |
          |         +---------------------------------+
          |---------| Keyword Analysis & Decision    |
          |         | (Based on input parsing and    |
          |         | predefined descriptions)       |
          |         +---------------------------------+
          |
          v
+-------------------+          +-------------------+
| Destination Chain |          | Destination Chain |
| (Hours)           |          | (Reservation)     |
+-------------------+          +-------------------+
          |                           |
          v                           v
+-------------------+          +-------------------+
| Response for Hours|          | Response for      |
| of Operation      |          | Book Reservation  |
+-------------------+          +-------------------+
          |                           |
          v                           v
+-------------------+
|      User         |
+-------------------+

"""

from langchain.chains.router import MultiPromptChain
from langchain.chains.router.llm_router import LLMRouterChain, RouterOutputParser
from langchain.chains.router.multi_prompt_prompt import MULTI_PROMPT_ROUTER_TEMPLATE
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain 

# Step 1: Prepare Prompts and System messages
# Define prompt templates
hours_template = "You are a librarian. The library's current hours of operation are from 6 AM to 13 PM."
reservation_template = "You are a librarian. To reserve a book, please visit our website(lib.com) or call our main desk.(665-777-7777)"

# Add a general info template as a fallback
general_info_template = "You are a librarian. I'm here to help with general inquiries. How can I assist you today?"

# Store information about each prompt in a list of dictionaries
prompt_infos = [
    {
        "name": "Hours",
        "description": "questions about library operation hours",
        "prompt_template": hours_template
    },
    {
        "name": "Reservation",
        "description": "questions about how to reserve a book",
        "prompt_template": reservation_template
    },
    {
        "name": "General Info",
        "description": "general library information and other inquiries",
        "prompt_template": general_info_template
    }
]


# Step 2: Prepare destination chains for each case

destination_chains = {}

for p_info in prompt_infos:
    # Create a prompt_template, later to compose a chain (prompt + llm)
    prompt = PromptTemplate.from_template(template=p_info["prompt_template"])
    # Create an actual chain
    chain = LLMChain(llm = llm, prompt = prompt)
    # store the chain for later access by key
    destination_chains[p_info["name"]] = chain 

# Create a string of destination names and descriptions formatted for the router template.
# This is used in the router's decision-making process to determine where to route a query.
destinations_str = ', '.join([f"{p['name']}: {p['description']}" for p in prompt_infos])

# setup router
router_template = MULTI_PROMPT_ROUTER_TEMPLATE.format(
    destinations = destinations_str
    )

router_prompt = PromptTemplate(template=router_template,
                               input_variables=["input"],
                               output_parser=RouterOutputParser())

# create a router_chain responsible for redirections

router_chain = LLMRouterChain.from_llm(llm=llm,prompt=router_prompt)

# creating the default chain
default_prompt = PromptTemplate.from_template("{input}")
default_chain = LLMChain(llm=llm, prompt=default_prompt)
# top Level combo

combined_chain = MultiPromptChain(
    router_chain=router_chain,
    destination_chains=destination_chains,
    default_chain=default_chain,
    verbose=True
)

# Example usage: Testing with different queries
queries = ["What are the library's hours?", "How do I reserve a book?", "Tell me more about the library services."]
for query in queries:
    response = combined_chain.invoke(input=query)
    print(f"Query: {query}\nResponse: {response}\n")