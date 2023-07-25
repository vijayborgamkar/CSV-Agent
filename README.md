## Language Chain Chatbot for CSV, Excel etc

This repository contains a Python script that implements a language chain chatbot for analyzing Pokémon data. The chatbot uses the Language Chain library, which incorporates OpenAI's powerful language models to interact with users and answer questions related to the Pokémon dataset.

Prerequisites
Before running the script, ensure you have the following libraries installed:

- pandas
- langchain
- IPython
- openai

You can install these libraries using pip:

`pip install pandas langchain openai`

#### How it works

The script allows you to interact with the Pokémon dataset by asking questions in natural language. It utilizes the Language Chain library, which provides two agents:

1. create_csv_agent(OpenAI(temperature=0), "pokemon.csv", verbose=True): This agent uses the GPT-3 language model provided by OpenAI to answer your questions based on the Pokémon dataset stored in a CSV file named pokemon.csv.
2. create_csv_agent(ChatOpenAI(temperature=0, model_name="gpt-4"), "pokemon.csv", verbose=True): This agent employs the GPT-4 language model, also provided by OpenAI, to respond to your queries.

#### Getting Started
1. Clone this repository to your local machine or download the script.py file.
2. Set up your OpenAI API key by assigning it to the OPENAI_API_KEY environment variable.
3. Ensure you have a dataset in one of the following formats: CSV, Excel (XLSX), JSON, or Google BigQuery (GBQ). For this example, a Pokémon dataset in CSV format is provided through a link.
4. Replace the file_path variable in the run_code function with the link to your dataset. For example, if you have a local file named pokemon.csv, you can set file_path = 'pokemon.csv'.
5. Execute the script using a Python interpreter.

#### Interacting with the Chatbot
Once the script is running, the chatbot will prompt you to enter your questions in natural language. Type your question and press "Enter" to receive the answer.

To end the conversation and exit the chatbot, type 'exit' (case-insensitive) and press "Enter".

#### Supported File Formats
The read_file function in the script supports the following file formats:

- CSV
- Excel (XLSX)
- JSON
- Google BigQuery (GBQ)
  
Please note that only files with the mentioned formats are compatible with this chatbot.


#### Example Usage

`os.environ["OPENAI_API_KEY"] = "YOUR_OPENAI_API_KEY"`

`file_path = 'https://gist.githubusercontent.com/armgilles/194bcff35001e7eb53a2a8b441e8b2c6/raw/92200bc0a673d5ce2110aaad4544ed6c4010f687/pokemon.csv'`

`file_extension = 'csv'`

`run_code(file_path, file_extension)`


Feel free to experiment with different questions related to the Pokémon dataset and explore the responses provided by the chatbot!

#### Note
The accuracy and quality of responses depend on the language model's training and the data available in the Pokémon dataset. For more accurate results, consider fine-tuning the language model on a more domain-specific dataset.

Enjoy interacting with your Pokémon data using the Language Chain chatbot! If you have any questions or face any issues, please open an issue in this repository.


Please ensure you comply with the terms of use of the OpenAI API and respect the data usage rights of the Pokémon dataset.
