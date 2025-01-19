# app.py
import gradio as gr
from app.components.langchain import langchain_interface
from app.components.vector_search import vector_search_interface
from app.components.ml_inference import ml_inference_interface

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

    demo.launch(server_name="0.0.0.0", server_port=7860)

if __name__ == "__main__":
    main()
