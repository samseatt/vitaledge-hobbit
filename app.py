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
    with gr.Blocks() as demo:
        gr.Markdown("# Hobbit: Admin UI for Mantle Operations")
        with gr.Tab("RAG Operations"):
            gr.Markdown("This is the RAG Operations tab.")
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
        with gr.Tab("ML Operations"):
            gr.Markdown("This section supports existing ML Operations.")
            with gr.Tab("My ML Inference"):
                ml_inference_interface()
        with gr.Tab("LangChains"):
            gr.Markdown("This supports constructing new LangChains.")
            with gr.Tab("My LangChain"):
                ml_inference_interface()
        with gr.Tab("ML Models"):
            gr.Markdown("This section supports constructing with new ML models.")
            with gr.Tab("My ML Model"):
                ml_inference_interface()
        with gr.Tab("Datalake"):
            gr.Markdown("This section supports direct datalake queries.")
            with gr.Tab("My Queries"):
                ml_inference_interface()

    demo.launch(server_name="0.0.0.0", server_port=7860)

if __name__ == "__main__":
    main()
