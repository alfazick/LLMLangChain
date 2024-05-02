# Using Pydantic to extract multiple fields from the output string of an LLM

from typing import List
#Init setup
from config_settings import API_KEY
from langchain_openai import OpenAI

llm = OpenAI(api_key=API_KEY,temperature=0.0)



from langchain.output_parsers import PydanticOutputParser
from langchain.prompts import PromptTemplate
from langchain.pydantic_v1 import BaseModel, Field, validator

class Author(BaseModel):
    number: int = Field(description="number of books written by the author")
    books: List[str] = Field(description="list of books they wrote")


user_query = "Generate the books written by Dan Brown."

# defining the output parser
output_parser =  PydanticOutputParser(pydantic_object=Author)

# defining the prompt template with parser instructions
prompt = PromptTemplate(
    template="Answer the user query.\n{format_instructions}\n{query}\n",
    input_variables=["query"],
    partial_variables={"format_instructions":output_parser.get_format_instructions()},
)

# defining the prompt 
my_prompt = prompt.format_prompt(query=user_query)

output = llm.invoke(my_prompt.to_string())

res = output_parser.parse(output)

print(res)