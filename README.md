# MultiAgentBot

A modular, agentic AI chatbot framework built with LangGraph, LangChain, and Streamlit. Integrates third-party tools (Wikipedia, Arxiv, FAISS vector store) for advanced information retrieval and research.

## Features
- Chatbot with LLM (Groq API)
- Tool-augmented chat: Wikipedia, Arxiv, and custom vector search
- State management with LangGraph and TypedDict
- Streamlit UI for easy interaction
- Modular, extensible codebase

## Setup
1. Clone this repo:
   ```sh
   git clone https://github.com/govindcss/MultiAgentBot.git
   cd MultiAgentBot
   ```
2. Install dependencies:
   ```sh
   pip install -r requirements.txt
   ```
3. Run the app:
   ```sh
   streamlit run app.py
   ```

## Usage
- Enter your Groq API key and select a model in the sidebar.
- Choose a use case: Basic Chatbot, Chatbot with Tool, Chatbot with Wikipedia, Chatbot with Arxiv.
- For tool-augmented chat, enter queries that require external information (e.g., "arXiv:2504.04022").

## License
Apache 2.0. See [LICENSE](LICENSE).

---

> Built by Govind, 2025. Contributions welcome!

