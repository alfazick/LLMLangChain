
from langchain_community.document_loaders import TextLoader

loader = TextLoader("text1.txt")
document = loader.load()

print(document)

loader2 = TextLoader("text2.txt")
document2 = loader2.load()

print(document2)


from langchain.document_loaders.csv_loader import CSVLoader

loader = CSVLoader(file_path='imaginary.csv')
data = loader.load()

print(data)

# from langchain.document_loaders import PyPDFLoader

# loader = PyPDFLoader("inputDocument.pdf")
# pages = loader.load_and_split()
