# components/datalake_ui.py
import gradio as gr
from app.services.datalake_service import DatalakeService

async def search_variants(study_id):
    datalake = DatalakeService()
    results = await datalake.search_variants(study_id)
    return results

def datalake_ui():
    study_id_input = gr.Number(label="Study ID", value=103)
    output = gr.JSON(label="Datalake Variants")
    button = gr.Button("Search Variants")

    button.click(search_variants, inputs=[study_id_input], outputs=[output])
    return gr.Interface(fn=search_variants, inputs=[study_id_input], outputs=[output])
