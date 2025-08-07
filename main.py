import pandasai as pai
from dotenv import load_dotenv
from pandasai_openai import AzureOpenAI
import os
from pandasai import DataFrame

load_dotenv()

AZURE_OPENAI_ENDPOINT = os.getenv("AZURE_OPENAI_ENDPOINT")
AZURE_OPENAI_API_TOKEN = os.getenv("AZURE_OPENAI_API_TOKEN")
AZURE_OPENAI_DEPLOYMENT_NAME = os.getenv("AZURE_OPENAI_DEPLOYMENT_NAME")
AZURE_OPENAI_API_VERSION = os.getenv("AZURE_OPENAI_API_VERSION")

llm = AzureOpenAI(
    azure_endpoint=AZURE_OPENAI_ENDPOINT,
    api_token=AZURE_OPENAI_API_TOKEN,
    deployment_name=AZURE_OPENAI_DEPLOYMENT_NAME,
    api_version=AZURE_OPENAI_API_VERSION
)

pai.config.set({
    "llm": llm,
    "save_logs": False,
    "save_charts": False
})

def create_description(file, prompt):
    print(file)
    df = pai.read_excel(file)
    response = df.chat(prompt)
    return response