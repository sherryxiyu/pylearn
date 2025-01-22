from langchain.vectorstores import Chroma
from langchain.embeddings import OllamaEmbeddings
from langchain.document_transformers import LongContextReorder
from langchain.chains.combine_documents import stuff

embeddings = OllamaEmbeddings(model_name="ollama_embedding")

texts = [
    "Basquetball",
    "fly me to the moon",
    "The Celltics are my favorite team",
    "This is a document about the Boston Celtics",
    "I simply love going to the movies",
    "The Boston Celtics won the game by 20 points",
    "This is just a random text",
    "Elden Ring is one of the best games in the last 15 years",
    "L..kornet is one of the best Celtics players",
    "Larry Bird"
]

retriver = Chroma.from_texts(texts, embedding=embeddings).as_retriever(
    search_kwargs={"k":10}
)

query="what can you tell me about Celtics?"

docs = retriver.get_relevant_documents(query)

#较不相关的放到中间，较相关的放到开始和结束
reordering = LongContextReorder()
reordered_docs = reordering.transform_documents(docs)

from langchain.prompts import PromptTemplate
from langchain_community.llms import Ollama
document_prompt = PromptTemplate(
    input_variables=["page_content"], template="{page_content}"
)
document_variable_name = "context"

stuff_prompt_override = """给定以下文本：
--------
{context}
--------
请回答以下问题：
{query}"""

prompt = PromptTemplate(
    template=stuff_prompt_override, input_variables=["context", "query"]
)

llm_chain = prompt | Ollama()

chain = stuff.create_stuff_documents_chain(
    llm_chain=llm_chain,
    document_prompt=document_prompt,
    document_variable_name=document_variable_name,
)
chain.run(input_documents=reordered_docs, query=query)