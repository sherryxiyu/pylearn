from langchain_community.document_loaders import DirectoryLoader

loader = DirectoryLoader("D:\lava", glob="**/*.md", show_progress=True, use_multithreading=True)
docs = loader.load()

#还有很多其他类型的loader
from langchain.document_loaders import PythonLoader, UnstructuredHTMLLoader