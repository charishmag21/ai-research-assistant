import chromadb
from chromadb.utils import embedding_functions

class ChromaMemory:
    def __init__(self, collection_name="memory"):
        self.client = chromadb.Client()
        self.collection = self.client.get_or_create_collection(
            name=collection_name,
            embedding_function=embedding_functions.DefaultEmbeddingFunction()
        )

    def save(self, query: str, answer: str):
        self.collection.add(documents=[answer], metadatas=[{"query": query}], ids=[query])

    def retrieve(self, query: str, top_k: int = 3):
        results = self.collection.query(query_texts=[query], n_results=top_k)
        return results.get("documents", [[]])[0]
