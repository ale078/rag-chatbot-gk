# RAG Chatbot - Vibe Coding

A local RAG chatbot built with Ollama, Chroma, LangChain and Streamlit.

## How to use

1. **Install Ollama and pull the model:**
   ```bash
   ollama pull llama3.1
   ```

2. **Setup the environment:**
   ```bash
   python -m venv venv
   .\venv\Scripts\activate
   pip install -r requirements.txt
   ```

3. **Add your documents:**
   Place your PDF files in the `pdfs/` folder.

4. **Run the application:**
   ```bash
   streamlit run app.py
   ```

## Tech Stack
- **LLM**: Llama 3.1 (via Ollama)
- **Orchestration**: LangChain
- **Vector Store**: ChromaDB
- **UI**: Streamlit
