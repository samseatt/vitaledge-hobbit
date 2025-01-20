# components/embeddings_ui.py
import gradio as gr
from app.services.vectordb_service import VectorDBService

async def generate_embedding(query_vector, top_k):
    vectorDB = VectorDBService()
    results = await vectorDB.search_vectors(query_vector, top_k)
    return results

def vectordb_ui():
    # study_id_input = gr.Number(label="Study ID", value=103)
    # output = gr.JSON(label="Datalake Variants")
    # button = gr.Button("Search Variants")

    # button.click(search_variants, inputs=[study_id_input], outputs=[output])
    # return gr.Interface(fn=search_variants, inputs=[study_id_input], outputs=[output])
    return []