import os
from openai import AzureOpenAI
from dotenv import load_dotenv
from src.sys_prompt import mc_prompt_v1
import pandas as pd

load_dotenv()
endpoint = os.getenv("ENDPOINT_URL")
deployment = os.getenv("DEPLOYMENT_NAME_1")
endpoint = os.getenv("ENDPOINT_URL")
subscription_key = os.getenv("AZURE_OPEN_AI_API_KEY")

# Initialize Azure OpenAI Service client with key-based authentication
client = AzureOpenAI(
    azure_endpoint=endpoint,
    api_key=subscription_key,
    api_version="2024-05-01-preview",
)

# Import data
df = pd.read_excel(
    path=r"/Users/harshgarg/Desktop/mc-lm-genai/data/LM Applications.xlsx"
)

df["emotion"] = ""
df["purpose"] = ""
df["commitment"] = ""

# Prepare the chat prompt
chat_prompt = [{"role": "user", "content": [{"type": "text", "text": mc_prompt_v1}]}]

for index, value in enumerate(df):
    # Include speech result if speech is enabled
    messages = chat_prompt

    # Generate the completion
    completion = client.chat.completions.create(
        model=deployment,
        messages=messages,
        max_tokens=800,
        temperature=0.7,
        top_p=0.95,
        frequency_penalty=0,
        presence_penalty=0,
        stop=None,
        stream=False,
    )

    print(completion.choices[0].message.content)
