
from langchain_community.document_loaders import TextLoader
from langchain_text_splitters.character import RecursiveCharacterTextSplitter
from langchain.schema import Document  # Assuming Document is a class you have or need

# Initialize the text splitter with desired settings
text_splitter = RecursiveCharacterTextSplitter(
    chunk_size=1000,
    chunk_overlap=200,
    add_start_index=True
)


# Load documents and extract them from the list
loader = TextLoader("text1.txt")
loaded_documents1 = loader.load()
document1 = loaded_documents1[0] if loaded_documents1 and isinstance(loaded_documents1, list) else None

loader2 = TextLoader("text2.txt")
loaded_documents2 = loader2.load()
document2 = loaded_documents2[0] if loaded_documents2 and isinstance(loaded_documents2, list) else None

documents = list()
# Check if both documents are properly loaded and are Document instances
if isinstance(document1, Document) and isinstance(document2, Document):
    # List of documents to be split
    docs = [document1, document2]
    # Split the documents
    try:
        documents = text_splitter.split_documents(docs)
        
    except Exception as e:
        print("Error during document splitting:", e)
else:
    print("Documents are not loaded correctly or are not instances of Document.")

print(documents)

import sys
import os

# Add the root directory to the Python path
# Assuming your script is run from /workspaces/LLMLangChain/03Chains
sys.path.append('/workspaces/LLMLangChain')

from config_settings import API_KEY

from langchain_openai import OpenAIEmbeddings
from langchain_community.vectorstores import FAISS

embeddings = OpenAIEmbeddings(api_key=API_KEY)
db = FAISS.from_documents(documents, embeddings)
# user query
query = "RUST"

docs = db.similarity_search(query)

print(docs)
embedded_query = embeddings.embed_query(query)
docs = db.similarity_search_by_vector(embedded_query)
print(docs)

# Next Retrievers
retriever = db.as_retriever()
docs = retriever.invoke(query)
print(docs)
