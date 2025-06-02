from langchain_community.tools.tavily_search import TavilySearchResults
from langgraph.prebuilt import ToolNode
from src.langgraphagenticai.tools.wikipedia_tool import get_wikipedia_tool
from src.langgraphagenticai.tools.arxiv_tool import get_arxiv_tool
from src.langgraphagenticai.tools.vectorstore_tool import get_vectorstore_tool

def get_tools():
    """
    Return the list of tools to be used in the chatbot, including Wikipedia, Arxiv, and VectorStore.
    """
    tools = [
        TavilySearchResults(max_results=2),
        get_wikipedia_tool(),
        get_arxiv_tool(),
        get_vectorstore_tool()
    ]
    return tools

# Tool condition functions for LangGraph

def wikipedia_tool_condition(state):
    """
    Returns True if the user query is best answered by Wikipedia (e.g., general knowledge, definitions).
    """
    user_input = state["messages"][-1].content.lower() if state["messages"] else ""
    keywords = ["wikipedia", "who is", "what is", "history of", "define", "definition"]
    return any(kw in user_input for kw in keywords)

def arxiv_tool_condition(state):
    """
    Returns True if the user query is best answered by Arxiv (e.g., research papers, scientific topics).
    """
    user_input = state["messages"][-1].content.lower() if state["messages"] else ""
    keywords = ["arxiv", "research paper", "study", "scientific", "journal", "publication"]
    return any(kw in user_input for kw in keywords)

def create_tool_node(tools):
    """
    creates and returns a tool node for the graph
    """
    return ToolNode(tools=tools)


