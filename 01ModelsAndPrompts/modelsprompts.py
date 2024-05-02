
from config_settings import API_KEY


# # Models: 1.LLM

# from langchain_openai import OpenAI

# llm = OpenAI(api_key = API_KEY)

# # Query the model
# response = llm.invoke("Who is the strongest chess player?")
# print(response)

# 2.Chat Model
# from langchain_openai import ChatOpenAI
# from langchain.schema.messages import HumanMessage, SystemMessage

# # Init chat
# chat = ChatOpenAI(api_key = API_KEY)

# # Defines a context and query using SystemMessage and HumanMessage
# messages = [
#     SystemMessage(content="You are a strong security software engineer"),
#     HumanMessage(content="How to read a file in Python?"),
# ]

# response = chat.invoke(messages)
# print(response.content)

# Prompt templates serve as predefined recipes for crafting prompts tailored for 
# language models and are reusable. A prompt template may include the following:

# Instructions: This provides specific guidelines that instruct the language model 
# on how to generate responses to queries.

# Few-shot examples: This provides examples of input-output pairs that help 
# the language model understand the context for the given prompt.

# User input: This corresponds to the user’s query.

# Basic Prompt Template
# from langchain_openai import OpenAI

# from langchain.prompts import PromptTemplate


# llm = OpenAI(api_key = API_KEY)


# tutor_template = """
#     Create a lesson plan on {topic}
#     in {programming_language} for the {audience}
#     lesson time is {time}
#     finish the lessson with assignments on {topic},
#     provide real coding examples
#     """

# tutor_template = PromptTemplate.from_template(tutor_template)

# message = tutor_template.format(topic = "for loops",
#                                 programming_language="C++",
#                                 audience="Fresh undegraduate",
#                                 time="1 hour 15 minutes",
#                                 )

# print(message)

# response = llm.invoke(message)
# with open('lesson_plan_output.txt', 'w', encoding='utf-8') as file:
#     file.write(response)  # Write the response directly to the file

# print(response)

# Few-shot prompt templates

examples = [
  {
    "review": "I absolutely love this product! It exceeded my expectations.",
    "sentiment": "Positive"
  },
  {
    "review": "I'm really disappointed with the quality of this item. It didn't meet my needs.",
    "sentiment": "Negative"
  },
  {
    "review": "The product is okay, but there's room for improvement.",
    "sentiment": "Neutral"
  }
]

from langchain_openai import ChatOpenAI
from langchain.prompts.few_shot import FewShotPromptTemplate
from langchain.prompts import PromptTemplate


chat  = ChatOpenAI(temperature=0.0,api_key = API_KEY) # temperature defines determinism

example_prompt = PromptTemplate(
    input_variables=["review","sentiment"],
    template="Review: {review}\n{sentiment}"
)

prompt = FewShotPromptTemplate(
    examples = examples,
    example_prompt=example_prompt,
    suffix="Review: {input}",
    input_variables=["input"]
)

message = prompt.format(input="The machine worked okay without much trouble.")

response = chat.invoke(message)
print(response.content)