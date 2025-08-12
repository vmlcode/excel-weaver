import gradio as gr
from main import create_description

DEFAULT_PROMPT = """You are a data analyst performing an initial review of a file for a key business decision.
Examine the provided Excel file and create a brief metadata summary (up to 5 sentences) that covers the following:
1. **Data Topic & Purpose**: What the dataset includes and its intended use.
2. **Key Structure**: List main columns with their data types (text/numeric/date) and important value ranges (date spans, min/max values). ALWAYS specify the actual value for single-value columns (e.g., "Brand: Apple", "Media Channel: Instagram") rather than stating "1 unique" or "single value"
3. **Notable Patterns**: Find 1-2 significant insights like common categories, outliers, trends, or data quality issues.
Format: Plain text only. No code blocks, images, or charts.
This summary will help determine if the file is suitable for further analysis."""


# Create Gradio interface
iface = gr.Interface(
    fn=create_description,
    inputs=[
        gr.File(label="Upload your Excel file", file_types=[".xlsx", ".xls", ".csv"]),
        gr.Textbox(
            label="Analysis Prompt", 
            value=DEFAULT_PROMPT,
            lines=10,
            max_lines=20
        ),
    ],
    outputs=gr.Textbox(label="Analysis Results", lines=10, max_lines=20),
    title="Excel Data Analyzer with PandasAI",
    description="Upload an Excel file and provide a prompt to generate metadata analysis. The tool will handle various Excel formats and provide fallback options if needed."
)

if __name__ == "__main__":
    iface.launch()