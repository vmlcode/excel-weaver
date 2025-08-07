import gradio as gr

from main import create_description

DEFAULT_PROMPT = """
DO NOT ADD CODE IMAGES OR CHARTS TO THE RESPONSE ONLY USE TEXT AND THE FOLLOWING INSTRUCTIONS
Using the provided Excel file, generate a metadata summary (no more than 5 sentences) that covers:
  1. Overall purpose or topic of the data.
  2. Sheet names and Year of the info
  3. Key columns (names + data types) and any important ranges (e.g. date spans, numeric min/max).
  5. One or two notable insights (e.g., dominant category, outlier, or trend).

Be concise but precise—this summary will help decide whether to load and use the file."""

gr.Interface(
    fn=create_description,
    inputs=[
        gr.File(label="Upload your file"),
        gr.TextArea(label="Write your Prompt Here", value=DEFAULT_PROMPT ),
    ],
    outputs=gr.TextArea(label="Answer from LLM"),
    title="PandasAI Metadata Prompt Test",
    description="Add an excel file and a prompt to generate a metadata description using the prompt below \n V. Maldonado (SalesfactoryAI)"
).launch()

