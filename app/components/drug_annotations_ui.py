# app/components/drug_annotations_ui.py
import gradio as gr
from app.services.datalake_service import DatalakeService

def drug_annotations_ui():
    with gr.Blocks() as drug_ui:
        gr.Markdown("## Explore Drug Annotations")

        # Inputs and table outputs
        subject_input = gr.Textbox(label="Subject ID", interactive=True)
        drug_input = gr.Textbox(label="Drug ID", interactive=True)
        annotation_output = gr.Dataframe(label="Annotations", headers=["Variant ID", "Annotation ID", "Timestamp"])
        details_output = gr.JSON(label="Annotation Details")

        # Search drug annotations
        async def search_annotations(subject_id, drug_id):
            annotations = await DatalakeService.fetch_drug_variants(subject_id, int(drug_id))
            return annotations

        # Fetch details for annotation
        async def fetch_annotation_details(annotation_id):
            return await DatalakeService.fetch_pharmacogenomic_annotation(int(annotation_id))

        search_button = gr.Button("Search")
        search_button.click(search_annotations, inputs=[subject_input, drug_input], outputs=[annotation_output])

        # Load details for selected annotation
        annotation_output.change(fetch_annotation_details, inputs=[annotation_output], outputs=[details_output])

    return drug_ui
