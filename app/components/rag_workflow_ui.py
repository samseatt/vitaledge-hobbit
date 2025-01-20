# app/components/rag_workflow_ui.py
import gradio as gr
from app.services.rag_orchestrator import RAGOrchestrator

async def run_rag(query):
    orchestrator = RAGOrchestrator()
    result = await orchestrator.run(query)
    return result

def rag_workflow_ui():
    query_input = gr.Textbox(label="Query", placeholder="Enter your query")
    output = gr.JSON(label="RAG Workflow Output")
    button = gr.Button("Run RAG Workflow")

    button.click(run_rag, inputs=[query_input], outputs=[output])
    return gr.Interface(fn=run_rag, inputs=[query_input], outputs=[output])
