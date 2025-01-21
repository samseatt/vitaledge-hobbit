import gradio as gr
from app.services.datalake_service import DatalakeService

async def load_subjects():
    """
    Fetches the list of subjects from the Datalake API.
    """
    service = DatalakeService()
    subjects = await service.get_all_subjects()
    return {subject["id"]: subject["name"] for subject in subjects}

async def load_subject_studies(subject_id: int):
    """
    Fetches studies for the selected subject.
    """
    service = DatalakeService()
    studies = await service.get_subject_studies(subject_id)
    return studies

def genomic_studies_ui():
    """
    Renders the Genomic Studies UI.
    """
    with gr.Blocks() as genomic_studies_section:
        gr.Markdown("## Genomic Studies Explorer")

        # Subject Selector
        subject_selector = gr.Dropdown(
            label="Select Subject",
            interactive=True,
            value=None,  # Leave empty or `None` to show the label by default
            choices=[],  # Populate dynamically when subjects are fetched
        )

        # Study Results Table
        study_results = gr.Dataframe(
            headers=["Study Name", "Description", "Genetic Score", "Percentile"],
            datatype=["str", "str", "number", "number"],
            interactive=False,
            label="Subject's Studies",
        )

        # Event Handlers
        subject_selector.change(
            load_subject_studies,
            inputs=[subject_selector],
            outputs=[study_results],
        )

        # Use Blocks.load() to populate the dropdown dynamically
        def populate_subject_selector():
            subjects = load_subjects()  # Fetch subjects dynamically
            return gr.Dropdown.update(choices=subjects)


        # Load subjects on startup
        genomic_studies_section.load(load_subjects, outputs=subject_selector)

    return genomic_studies_section


"""
# Example code:

def load_subjects():
    # Replace this with your actual data-fetching logic
    return ["Subject 1", "Subject 2", "Subject 3"]

with gr.Blocks() as demo:
    subject_selector = gr.Dropdown(
        label="Select Subject",
        interactive=True,
    )

    # Use Blocks.load() to populate the dropdown dynamically
    def populate_subject_selector():
        subjects = load_subjects()  # Fetch subjects dynamically
        return gr.Dropdown.update(choices=subjects)

    demo.load(populate_subject_selector, outputs=subject_selector)

"""