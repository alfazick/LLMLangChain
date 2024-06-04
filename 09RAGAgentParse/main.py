import html_retriever

file_name = "page1.txt"

html_txt = html_retriever.get_html(file_name)

from langchain_openai import ChatOpenAI

import sys
sys.path.append('/workspaces/LLMLangChain')
from config_settings import API_KEY

# defining the LLM model

llm = ChatOpenAI(
    openai_api_key = API_KEY,
    model_name='gpt-3.5-turbo',
    temperature=0.0
)

from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain 

# creating the prompt template

prompt_template = PromptTemplate(
    input_variables=["html"],
    template="Identify text ids for Given the html {html}.",
)

from langchain_community.document_loaders import TextLoader
from langchain_text_splitters.character import RecursiveCharacterTextSplitter

from langchain_openai import OpenAIEmbeddings
from langchain_chroma import Chroma
from langchain.chains import ConversationalRetrievalChain
from langchain.memory import ConversationBufferWindowMemory

from langchain.agents import Tool 
from langchain.agents import initialize_agent


txt_loader = TextLoader(file_name)
my_txt = txt_loader.load()

# defining the splitter
document_splitter = RecursiveCharacterTextSplitter(
    chunk_size = 300,
    chunk_overlap = 70
)

# splitting the document
docs = document_splitter.split_documents(my_txt)

# print(docs)

# embedding the chunks to vector stores
embeddings = OpenAIEmbeddings(openai_api_key = API_KEY)

persist_directory = "db"

my_database = Chroma.from_documents(
    documents = docs,
    embedding = embeddings,
    persist_directory = persist_directory
)

# defining the conversational memory

retaining_memory = ConversationBufferWindowMemory(
    memory_key="chat_history",
    k = 5,
    return_messages=True
)

# defining the retriever
question_answering = ConversationalRetrievalChain.from_llm(
    llm,
    retriever = my_database.as_retriever(),
    memory = retaining_memory
)




# defining the tool for the agent
tools = [
    Tool(
        name="html_content",
        func = question_answering.run,
        description=("use this tool when only when user need to the list of the textrea id ")
    )
]


# initialize the agent
agent = initialize_agent(
    agent="chat-conversational-react-description",
    tools = tools,
    llm = llm,
    verbose = True,
    max_iterations = 3,
    early_stopping_method="generate",
    memory = retaining_memory
)


# prompt = "give me a list of all textarea ids which is located in html_content tool"

# # calling the agent
# while True:
#     question = input("Enter your query: ")
#     if question == "exit":
#         break
#     print(agent(question))