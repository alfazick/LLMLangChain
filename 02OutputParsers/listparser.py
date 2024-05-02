
from config_settings import API_KEY
from langchain_openai import OpenAI
from langchain.prompts import PromptTemplate
from langchain.output_parsers import CommaSeparatedListOutputParser


llm = OpenAI(api_key = API_KEY)


parser_List = CommaSeparatedListOutputParser()

partial_variables = {"format_instructions":parser_List.get_format_instructions()}

# creating our prompt template
template = """Provide the response in format {format_instructions} 
            to the user's question {question}"""


prompt_List = PromptTemplate.from_template(
    template=template,
    partial_variables=partial_variables,
)


question="List most common LLM latency improvement techniques"

print(llm.invoke(input=prompt_List.format(question = question)))


# 1. Caching, 
# 2. Compression, 
# 3. Domain Sharding, 
# 4. Image Optimization, 
# 5. Minification, 
# 6. Prefetching, 
# 7. Resource bundling, 
# 8. Server-side rendering, 
# 9. Content Delivery Networks (CDN), 
# 10. Load Balancing