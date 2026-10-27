import streamlit as st
from rag_pipeline import get_index, create_rag_chain

st.set_page_config(page_title="RAG Chatbot", page_icon="📚")
st.title("📚 My PDF Chatbot (LlamaIndex Version)")

if "query_engine" not in st.session_state:
    with st.spinner("Loading documents and creating index..."):
        index = get_index()
        if index:
            st.session_state.query_engine = create_rag_chain(index)
            st.success("Chatbot ready! Ask me anything about your PDFs.")
        else:
            st.warning("No documents found in 'pdfs' folder. Please add some PDFs and restart.")

question = st.text_input("Ask a question:")

if question:
    if "query_engine" in st.session_state:
        with st.spinner("Thinking..."):
            response = st.session_state.query_engine.query(question)
            st.markdown(f"**Answer:** {response}")
            
            with st.expander("View Sources"):
                for node in response.source_nodes:
                    st.write(f"Score: {node.score:.3f} | Text: {node.text[:200]}...")
    else:
        st.error("Please add documents to the 'pdfs' folder first.")

