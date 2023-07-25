import pandas as pd
from IPython.display import Markdown, display
from langchain.agents import create_csv_agent
from langchain.chat_models import ChatOpenAI
from langchain.llms import OpenAI
import os

os.environ["OPENAI_API_KEY"] = ""


def read_file(file_path, file_extension):
    if file_extension == 'csv':
        df = pd.read_csv(file_path)
    elif file_extension == 'xlsx':
        df = pd.read_excel(file_path)
    elif file_extension == 'json':
        df = pd.read_json(file_path)
    elif file_extension == 'gbq':
        df = pd.read_gbq(file_path)
    else:
        raise ValueError("Unsupported file format. Only .xlsx, .csv, .json, and .gbq files are supported.")

    return df


def run_code(file_path, file_extension):
    df = read_file(file_path, file_extension)

    # Load the agent
    agent = create_csv_agent(OpenAI(temperature=0), "pokemon.csv", verbose=True)

    gpt4_agent = create_csv_agent(
        ChatOpenAI(temperature=0, model_name="gpt-4"), "pokemon.csv", verbose=True
    )

    while True:
        user_input = input("Enter your question (type 'exit' to end): ")
        if user_input.lower() == 'exit':
            break

        agent.run(user_input)


file_path = 'https://gist.githubusercontent.com/armgilles/194bcff35001e7eb53a2a8b441e8b2c6/raw/92200bc0a673d5ce2110aaad4544ed6c4010f687/pokemon.csv'
file_extension = 'csv'

run_code(file_path, file_extension)
