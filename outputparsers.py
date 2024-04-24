# how to parse the output of an LLM using output parser in the LangChain framework

# parsers are a tool to get a structured output

# Types of parsers

# -> Datetime
# -> List
# -> Auto-fixing
# -> Enum 
# -> XML 
# -> Pydantic(JSON)
# -> structured output parser
# -> retry parse

from config_settings import API_KEY
from langchain_openai import OpenAI

# #1 Datetime parser Base example
# from langchain.output_parsers import DatetimeOutputParser
# parser_dateTime = DatetimeOutputParser()
# from langchain.prompts import PromptTemplate
# # creating a prompt template
# template = """Provide the response in format {format_instructions}
# to the user's question {question}"""

# # passing the format instructions of the parser to the template

# prompt_dateTime = PromptTemplate.from_template(
#     template,
#     partial_variables={"format_instructions": parser_dateTime.get_format_instructions()}
# )

# llm = OpenAI(api_key = API_KEY)
# response = llm.invoke(input=prompt_dateTime.format(question="When the US election day?"))
# parsed_date = parser_dateTime.parse(response)
# print(parsed_date)

# Datetime parser Scheduler

import datetime
from langchain.output_parsers import DatetimeOutputParser
from langchain.prompts import PromptTemplate



llm = OpenAI(api_key=API_KEY,temperature=0.0)


# Initialize the datetime parser with the correct format
datetime_parser = DatetimeOutputParser(format="%Y-%m-%dT%H:%M:%S.%fZ")

# Define the main template with a placeholder for format instructions
template = """Given today's date is {today_date}, what is the exact date and time for {phrase}? 
Return the date and time strictly in the specified format: {format_instructions}."""

# Create the PromptTemplate using from_template method
prompt_dateTime = PromptTemplate.from_template(
    template,
    partial_variables={"format_instructions": datetime_parser.get_format_instructions()}
)

# Define another template for use in a specific function
date_query_template = """Given today's date is {today_date}, 
what is the exact date and time for {phrase}? 
Return only the date and time strictly in ISO 8601 format: YYYY-MM-DDTHH:MM:SS.mmmmmmZ.
ONLY DATE, NO EXTRA WORDS"""

# Initialize the PromptTemplate with all required fields for this specific function
prompt_template = PromptTemplate(
    template=date_query_template,
    input_variables=['phrase', 'today_date']
)

# Meeting dictionary
meetings = {}

def add_meeting(date, name, time):
    meetings[date] = {"name": name, "time": time.strftime("%I:%M %p")}

def get_relative_date(reference_date, phrase):
    # Use the prompt template
    prompt = prompt_template.format(
        phrase=phrase,
        today_date=reference_date.strftime('%Y-%m-%d')
    )

    print("Formatted prompt:", prompt)

    response = llm.invoke(prompt)

    print("LLM Response:", response)

    try:
        # Strip any leading/trailing whitespaces before parsing
        parsed_date = datetime_parser.parse(response.strip())
        print("Parsed date:", parsed_date)
        return parsed_date 
    except Exception as e:
        print(f"Error parsing date: {str(e)}")
        return None

# Example: Adding a meeting
reference_date = datetime.datetime.now()
relative_date = get_relative_date(reference_date, "next Monday")

if relative_date:
    add_meeting(relative_date.date(), "Bob", relative_date)

print("Meetings scheduled:", meetings)
