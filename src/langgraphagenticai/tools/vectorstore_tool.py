from src.langgraphagenticai.vectorstore.vectorstore_faiss import VectorStoreManager
from langchain.tools.base import BaseTool
from typing import ClassVar

class VectorStoreQueryTool(BaseTool):
    name: ClassVar[str] = "vectorstore_query"
    description: ClassVar[str] = "Query the local FAISS vector store for relevant documents."

    def __init__(self, persist_path="./faiss_index"):
        super().__init__()
        self.manager = VectorStoreManager(persist_path=persist_path)

    def _run(self, query: str, k: int = 3):
        results = self.manager.query(query, k=k)
        return "\n".join([doc.page_content for doc in results])

    async def _arun(self, query: str, k: int = 3):
        return self._run(query, k)

def get_vectorstore_tool():
    return VectorStoreQueryTool()
