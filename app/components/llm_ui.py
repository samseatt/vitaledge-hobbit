import gradio as gr
from app.services.llm_service import LLMService

async def generate_text(prompt):
    llm = LLMService()
    results = await llm.generate_text(prompt)
    return results

def llm_ui():
    # study_id_input = gr.Number(label="Study ID", value=103)
    # output = gr.JSON(label="Datalake Variants")
    # button = gr.Button("Search Variants")

    # button.click(search_variants, inputs=[study_id_input], outputs=[output])
    # return gr.Interface(fn=search_variants, inputs=[study_id_input], outputs=[output])
    return "{}"