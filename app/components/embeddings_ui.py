# components/embeddings_ui.py
import gradio as gr
from app.services.embeddings_service import EmbeddingsService

async def generate_embedding(text):
    embeddings = EmbeddingsService()
    results = await embeddings.generate_embedding(text)
    return results

def embeddings_ui():
    # study_id_input = gr.Number(label="Study ID", value=103)
    # output = gr.JSON(label="Datalake Variants")
    # button = gr.Button("Search Variants")

    # button.click(search_variants, inputs=[study_id_input], outputs=[output])
    # return gr.Interface(fn=search_variants, inputs=[study_id_input], outputs=[output])
    return []