import os
import streamlit as st
from llama_index.core import VectorStoreIndex, SimpleDirectoryReader, StorageContext, load_index_from_storage
from llama_index.embeddings.ollama import OllamaEmbedding
from llama_index.llms.ollama import Ollama
from llama_index.core import Settings

# Configuración Global de Ollama
Settings.llm = Ollama(model="qwen2.5:3b", request_timeout=300.0)
Settings.embed_model = OllamaEmbedding(model_name="nomic-embed-text")

def get_index(pdf_folder="pdfs"):
    if not os.path.exists(pdf_folder):
        os.makedirs(pdf_folder)
        return None

    # Verificar si ya existe un índice persistido
    if os.path.exists("./storage"):
        storage_context = StorageContext.from_defaults(persist_dir="./storage")
        index = load_index_from_storage(storage_context)
        return index
    
    # Si no existe, cargar documentos y crear índice
    documents = SimpleDirectoryReader(pdf_folder).load_data()
    if not documents:
        return None
        
    index = VectorStoreIndex.from_documents(documents)
    index.storage_context.persist(persist_dir="./storage")
    return index

def create_rag_chain(index):
    if index is None:
        return None
    return index.as_query_engine(similarity_top_k=4)
