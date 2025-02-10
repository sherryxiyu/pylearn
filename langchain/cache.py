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

# use sqlite
from langchain.cache import SQLiteCache
langchain.llm_cache = SQLiteCache(database_path=".langchin.db")

start_time = time.time()
print(llm.predict("用中文讲个笑话"))
