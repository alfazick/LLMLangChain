
#  Example multi-step processing chain

import sys
import os

# Add the root directory to the Python path
# Assuming your script is run from /workspaces/LLMLangChain/03Chains
sys.path.append('/workspaces/LLMLangChain')



from config_settings import API_KEY
from langchain_openai import OpenAI


# defining LLM model
llm = OpenAI(api_key=API_KEY,temperature=0.0)

from langchain.chains import LLMChain 
from langchain.prompts import ChatPromptTemplate
from langchain.chains import SequentialChain

# Original input - user's description of the desired function
function_description = "I need a Python function that calculates the factorial of a number using recursion."


prompt_1 = ChatPromptTemplate.from_template(
    """Write a complete and runnable Python function based on this description. 
    The function should use recursion to calculate the factorial of a number:\n\n{description}"""
)

# The output here is the Python code for teh function
chain_1 = LLMChain(llm=llm,prompt=prompt_1,output_key="function_code")

# Creating the prompt template for the second chain - Document the function

prompt_2 = ChatPromptTemplate.from_template(
    """Provide detailed Python docstring documentation for the following Python function. 
    Include parameters, return type, and a brief example of how to use the function:\n\n{function_code}"""
)

# The output here is the documentation for the function
chain_2 = LLMChain(llm=llm, prompt=prompt_2, output_key="documentation")

# Creating the prompt template for the third chain - Write a test case
prompt_3 = ChatPromptTemplate.from_template(
    """Write a test function using Python's unittest framework for this Python function. 
    Include at least two test cases to verify correct functionality:\n\n{function_code}"""
)


# The output here is a test case for the function
chain_3 = LLMChain(llm=llm, prompt = prompt_3, output_key = "test_case")

# Creating the prompt template for the fourth chain - Suggest error handling
prompt_4 = ChatPromptTemplate.from_template(
    """Suggest specific error handling improvements for this Python function. 
    Include Python code snippets that could be added to the function 
    to prevent or manage errors:\n\n{function_code}"""
)


# The output here is error handling advice for the function
chain_4 = LLMChain(llm=llm, prompt=prompt_4, output_key="error_handling")

final_chain = SequentialChain(
    chains = [chain_1,chain_2,chain_3,chain_4],
    input_variables=["description"],
    output_variables=["function_code","documentation","test_case","error_handling"],
    verbose = True 
)

def pretty_print_results(results):
    print("Function Code:")
    print("--------------")
    print(results['function_code'])
    print("\nDocumentation:")
    print("--------------")
    print(results['documentation'])
    print("\nTest Case:")
    print("----------")
    print(results['test_case'])
    print("\nError Handling:")
    print("---------------")
    print(results['error_handling'])
    print("\n")

results = final_chain.invoke(function_description)
pretty_print_results(results)

with open('multiplechain.txt', 'w') as f:
    f.write("Function Code:\n")
    f.write(results['function_code'] + "\n\n")
    f.write("Documentation:\n")
    f.write(results['documentation'] + "\n\n")
    f.write("Test Case:\n")
    f.write(results['test_case'] + "\n\n")
    f.write("Error Handling:\n")
    f.write(results['error_handling'] + "\n")
