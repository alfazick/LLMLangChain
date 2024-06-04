from langchain_community.document_loaders import UnstructuredHTMLLoader


# dependency pip install unstructured

html_page = "page.html"

loader = UnstructuredHTMLLoader(html_page)

data = loader.load()

print(data)

html_page = "page_after.html"

loader = UnstructuredHTMLLoader(html_page)

data = loader.load()

print(data)