from typing import Annotated, Literal, Optional, List
from typing_extensions import TypedDict
from langgraph.graph.message import add_messages
from langchain_core.messages import HumanMessage, AIMessage

class State(TypedDict):
    """
    Represents the structure of the state used in the graph, including conversation history and context.
    """
    messages: Annotated[List[HumanMessage | AIMessage], add_messages]
    # Add more fields as needed for context management