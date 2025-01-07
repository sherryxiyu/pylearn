from langchain.prompts import SemanticSimilarityExampleSelector
from langchain_ollama import OllamaEmbeddings
from langchain_community.vectorstores import Chroma

examples = [{"input": "2+2", "output": "4"},
            {"input": "2+3", "output": "5"},
            {"input": "2+4", "output": "6"},
            {"input": "write a poem about moon", "output": "one for the moon, and one for mw"},]

to_vectorize = [" ".join(example.values()) for example in examples]
embeddings = OllamaEmbeddings(model="mxbai-embed-large", base_url="http://localhost:11434/")
vectorstore = Chroma.from_texts(to_vectorize, embeddings, metadatas=examples)
few_shot_prompt = SemanticSimilarityExampleSelector.from_examples(vectorstore_cls=vectorstore, k=1,
                                                                  embeddings=embeddings, Chroma=Chroma, examples=examples)
print(few_shot_prompt)
# selected_prompts2 = SemanticSimilarityExampleSelector.select_examples(vectorstore, input_variables=examples[0])
