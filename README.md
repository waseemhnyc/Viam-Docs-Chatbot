# Viam Docs Chatbot

**Work In Progress! [Follow for updates](https://twitter.com/waseemhnyc)**

This chatbot lets you ask the Viam docs questions to help you in your next Robotics project. We use Langchain to load data from the [Viam Robotics docs](https://github.com/viamrobotics/docs), embed the data and then find the relevant information based on the user's question. We pass that relevant information to OpenAI GPT4 with the question to generate a thoughtful answer.

## Ways to improve and future updates

1. Deploy a live app so anyone could access this chatbot
2. Embed and load documentation from the Python/Typescript/Go SDKs so chatbot could answer with more code examples
3. Integrate a Speech to Text and Text to Speech, so you could speak to the chatbot
4. Create a code assistant agent that will help develop your robotics application with Viam

Have an idea on how to improve? Please reach out!

## Questions, Follow for Updates or Get in Touch

Twitter: https://twitter.com/waseemhnyc

Email: waseemh.nyc@gmail.com


## Prerequisites

Before you begin, ensure you have met the following requirements:

- Installed a recent version of Python (3.7 or newer) installed and a way to create virtual environments (virtualenv or conda)
- Created OpenAI API account and obtain an OpenAI API key

## Getting Started

Clone the repo

```bash
git clone https://github.com/waseemhnyc/Viam-Docs-Chatbot
```

Create a virutalenv and source the environment

```bash
python3 -m venv myenv
source venv/bin/activate
```

Install the necessary libraries

```bash
pip install -r requirements.txt
```

Create a .env file and input your OpenAI API Key in the file

```bash
cp .env.example .env
```

Ingest and embed data

```bash
python ingest_data.py
```

## Usage

To run the program, run the following command in the terminal:

```bash
python app.py
```
