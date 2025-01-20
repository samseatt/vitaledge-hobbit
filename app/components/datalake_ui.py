# components/datalake_ui.py
import gradio as gr
from app.services.datalake_service import DatalakeService

async def get_subjects(study_id):
    datalake = DatalakeService()
    results = await datalake.get_subjects(study_id)
    return results

def datalake_ui():
    subject_id_input = gr.Number(label="Subject ID", value=1)
    output = gr.JSON(label="Datalake Subjects")
    button = gr.Button("Get Subjects")

    button.click(get_subjects, inputs=[subject_id_input], outputs=[output])
    return gr.Interface(fn=get_subjects, inputs=[subject_id_input], outputs=[output])
