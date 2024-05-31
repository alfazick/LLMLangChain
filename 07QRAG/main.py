
# Step 1: Load the file

from langchain_community.document_loaders import PyPDFLoader

# loading the document
filename = "cpu-intro.pdf"
loader = PyPDFLoader(filename)
mypdf = loader.load()

# Verify step 1
# print(mypdf)

# Step 2: Split the documents into chunks
from langchain.text_splitter import RecursiveCharacterTextSplitter

# define the splitter, kind of magic number
document_splitter = RecursiveCharacterTextSplitter(
    chunk_size = 300,
    chunk_overlap = 70
)

# splitting the document
docs = document_splitter.split_documents(mypdf)

# Verify step 2
# print(docs)


# Step3: Embed the documents to vectore store

import sys
import os
import pysqlite3 as sqlite3


# Add the root directory to the Python path
# Assuming your script is run from /workspaces/LLMLangChain/03Chains
sys.path.append('/workspaces/LLMLangChain')

from config_settings import API_KEY

from langchain_openai import OpenAIEmbeddings

from langchain_chroma import Chroma


embeddings = OpenAIEmbeddings(api_key=API_KEY)

# db = Chroma.from_documents(
#     documents=docs,
#     embedding=embeddings,
# )

# # Example Run

query = "What is a process?"
# docs = db.similarity_search(query)

# # print results
# print(docs[0].page_content)

# # 4
# # The Abstraction: The Process
# # In this chapter, we discuss one of the most fundamental abstract ions that
# # the OS provides to users: the process . The deﬁnition of a process, infor-
# # mally, is quite simple: it is a running program [V+65,BH70]. The program

# a. Load to Memory
db = Chroma.from_documents(
    documents=docs,
    embedding=embeddings,
    persist_directory="./chroma_db"
)

docs = db.similarity_search(query)
print(docs[0].page_content)

# Step 4 Define the retriever

# For chat create ConversationBufferWindowMemory with last 5 interactions


from langchain.memory import ConversationBufferWindowMemory

# defining the conversational memory
retaining_memory = ConversationBufferWindowMemory(
    memory_key="chat_history",
    k = 5,
    return_messages=True
)

from langchain.chains import ConversationalRetrievalChain
from langchain_openai import ChatOpenAI

# defining the model
llm = ChatOpenAI(
    openai_api_key=API_KEY,
    model_name='gpt-3.5-turbo',
    temperature=0.0
)


# define the retriever
QnA = ConversationalRetrievalChain.from_llm(
    llm,
    retriever = db.as_retriever(),
    memory = retaining_memory 
)


# defining the loop for a conversation with the AI
while True:
    question = input("Enter your query: ")
    if question == 'exit': 
        break 
    # getting the response
    result = QnA({"question": "Answer only in the context of the document provided." + question})
    print(result['answer'])


"""
The Abstraction: The Process
In this chapter, we discuss one of the most fundamental abstract ions that
the OS provides to users: the process . The deﬁnition of a process, infor-
mally, is quite simple: it is a running program [V+65,BH70]. The program

Enter your query: what is a process?
In the context of the document provided, a process is defined as 
a running program.

Enter your query: what is running program
A running program in the context of the document provided refers 
to a program that is actively executing on a computer system. 
It is mentioned that one often wants to run more than one program at once, 
such as a web browser, mail program, game, music player, etc. 
The document also discusses understanding the machine state of a program, 
which includes what parts of the machine are important to the execution of 
the program at any given time.

Enter your query: what is a computer system
In the context of the document provided, a computer system refers to a system that can seemingly 
run tens or even hundreds of processes at the same time, making it easy to use without 
the need to be concerned about CPU availability. The challenge highlighted is to manage and 
optimize the running of multiple processes efficiently.

Enter your query: what is CPU availability
In the context of the document provided, CPU availability refers to the challenge of 
providing the illusion of many CPUs despite having only a few physical CPUs available. 
The document discusses the technique of time-sharing the CPU to allow users 
to run multiple concurrent processes, even though there are limitations in physical CPU resources.

Enter your query: exit
"""