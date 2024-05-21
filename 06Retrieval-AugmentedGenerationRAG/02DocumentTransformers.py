
"""
Document transformers in LangChain play a crucial role in preparing data 
for processing by transforming documents into a format suitable 
for specific applications or models.
"""
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

# Check if both documents are properly loaded and are Document instances
if isinstance(document1, Document) and isinstance(document2, Document):
    # List of documents to be split
    docs = [document1, document2]
    # Split the documents
    try:
        all_splits = text_splitter.split_documents(docs)
        for split in all_splits:
            print(split)  # Assuming this prints something meaningful
    except Exception as e:
        print("Error during document splitting:", e)
else:
    print("Documents are not loaded correctly or are not instances of Document.")