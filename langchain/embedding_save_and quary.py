from langchain.embeddings import OllamaEmbeddings
from langchain.vectorstores import FAISS

list_text = [
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

db = FAISS.from_texts(list_text, OllamaEmbeddings())

# similarity_search
query = 'which team wons the game by 20 points?'
docs = db.similarity_search(query)

# similarity_search_by_vector
embedding_vector = OllamaEmbeddings().embed_query(query)
docs = db.similarity_search_by_vector(embedding_vector)

# similarity_search_with_score
docs_and_scores = db.similarity_search_with_score(query)

#save & load
db.save_local('faiss_index')
save_db = FAISS.load_local('faiss_index', OllamaEmbeddings())