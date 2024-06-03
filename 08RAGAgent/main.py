## Utilize RAG architecture to create own agent

from langchain_community.document_loaders import PyPDFLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter



from langchain_openai import OpenAIEmbeddings
from langchain_chroma import Chroma
from langchain.memory import ConversationBufferWindowMemory

from langchain_openai import ChatOpenAI

from langchain.chains import ConversationalRetrievalChain

import sys
sys.path.append('/workspaces/LLMLangChain')
from config_settings import API_KEY

# defining the model

llm = ChatOpenAI(
    openai_api_key = API_KEY,
    model_name='gpt-3.5-turbo',
    temperature=0.0
)



# loading the document
filename = "cpu-sched.pdf"
loader =  PyPDFLoader(filename)
mypdf = loader.load()

# defining the splitter
document_splitter = RecursiveCharacterTextSplitter(
    chunk_size = 300,
    chunk_overlap = 70
)

# splitting the document
docs = document_splitter.split_documents(mypdf)

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


# New part

from langchain.agents import Tool 
from langchain.agents import initialize_agent

# defining the tool for the agent
tools = [
    Tool(
        name="Knowledge Base",
        func = question_answering.run,
        description=("use this tool when answering questions related to the CPU scheduling")
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

# calling the agent
while True:
    question = input("Enter your query: ")
    if question == "exit":
        break
    print(agent(question))


