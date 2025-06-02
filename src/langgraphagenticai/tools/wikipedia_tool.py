from langchain_community.tools.wikipedia.tool import WikipediaQueryRun
from langchain_community.utilities.wikipedia import WikipediaAPIWrapper

def get_wikipedia_tool():
    """
    Returns a Wikipedia tool for information retrieval.
    """
    return WikipediaQueryRun(api_wrapper=WikipediaAPIWrapper())
