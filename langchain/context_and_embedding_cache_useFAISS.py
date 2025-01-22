from langchain.storage import InMemoryStore, LocalFileStore
from langchain.embeddings import CacheBackedEmbeddings
from langchain.document_loaders import TextLoader
from langchain.embeddings import OllamaEmbeddings
from langchain.text_splitter import CharacterTextSplitter
from langchain.vectorstores import FAISS

underlying_embeddings = OllamaEmbeddings()
fs = LocalFileStore("./cache/")

cached_embedder = CacheBackedEmbeddings.from_bytes_store(
    underlying_embeddings, fs, namespace=underlying_embeddings.model
)

raw_documents = TextLoader('documentstore/state_of_the_union.txt').load()
text_spliter = CharacterTextSplitter(chunk_size=1000, chunk_overlap=0)
documents = text_spliter.split_documents(raw_documents)

db = FAISS.from_documents(documents, cached_embedder)

# load cache
store = InMemoryStore()
underlying_embeddings = OllamaEmbeddings()
embedder = CacheBackedEmbeddings.from_bytes_store(
    underlying_embeddings, store, namespace=underlying_embeddings.model
)
embedings = embedder.embed_documents(['hello', 'goodbye'])
embedings_from_cache = embedder.embed_documents(['hello', 'goodbye'])

assert embedings == embedings_from_cache