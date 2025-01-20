# app.py
import gradio as gr
from app.components.langchain import langchain_interface
from app.components.vector_search import vector_search_interface
from app.components.ml_inference import ml_inference_interface
from app.components.datalake_ui import datalake_ui
from app.components.embeddings_ui import embeddings_ui
from app.components.vectordb_ui import vectordb_ui
from app.components.llm_ui import llm_ui
from app.components.rag_workflow_ui import rag_workflow_ui

def main():
    # Create the main Gradio interface
    with gr.Blocks() as demo:
        gr.Markdown("# Hobbit: Admin UI for Mantle Operations")

        with gr.Tab("LangChain Workflows"):
            langchain_interface()

        with gr.Tab("VectorDB Search"):
            vector_search_interface()

        with gr.Tab("ML Inference"):
            ml_inference_interface()

        with gr.Tab("Datalake"):
            datalake_ui()
            
        with gr.Tab("Embeddings"):
            embeddings_ui()

        with gr.Tab("VectorDB"):
            vectordb_ui()

        with gr.Tab("LLM"):
            llm_ui()
            
        with gr.Tab("RAG Workflow"):
            rag_workflow_ui()

    demo.launch(server_name="0.0.0.0", server_port=7860)

if __name__ == "__main__":
    main()
