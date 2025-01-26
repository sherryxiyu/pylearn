import time
from langchain.llms import ollama
import langchain

llm = ollama()
from langchain.cache import InMemoryCache
langchain.llm_cache = InMemoryCache()

start_time = time.time()
print(llm.invoke("tell me a joke"))
end_time = time.time()
during = start_time-end_time

# second time same question
start_time = time.time()
print(llm.invoke("tell me a joke"))
end_time = time.time()
during = start_time-end_time
