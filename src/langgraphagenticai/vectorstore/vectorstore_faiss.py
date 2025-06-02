from langchain_community.vectorstores import FAISS
from langchain_community.embeddings import HuggingFaceEmbeddings
import os

class VectorStoreManager:
    """
    Handles creation and retrieval of a FAISS vector store for document search and retrieval.
    """
    def __init__(self, persist_path="./faiss_index"):
        self.persist_path = persist_path
        self.embeddings = HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")
        self.vectorstore = None

    def create_vectorstore(self, documents):
        """
        Create a FAISS vector store from a list of documents (strings).
        """
        self.vectorstore = FAISS.from_texts(documents, self.embeddings)
        self.vectorstore.save_local(self.persist_path)
        return self.vectorstore

    def load_vectorstore(self):
        """
        Load an existing FAISS vector store from disk.
        """
        if os.path.exists(self.persist_path):
            self.vectorstore = FAISS.load_local(self.persist_path, self.embeddings)
            return self.vectorstore
        else:
            raise FileNotFoundError(f"No FAISS index found at {self.persist_path}")

    def query(self, query_text, k=3):
        """
        Query the vector store for the most similar documents to the input text.
        """
        if not self.vectorstore:
            self.load_vectorstore()
        return self.vectorstore.similarity_search(query_text, k=k)
