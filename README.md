# Tovar AI - Ask for football facts

Using Langchain agents and Streamlit to get fun football facts.

## What's up?

This is a project to participate in the Backdrop build v2 challenge (https://backdropbuild.com/v2).

The goal of this project is to build a control panel for football commentators to help them narrate fun facts about teams, players, referees and everything involved around the football match being narrated.

This also aims to prove the usefulness of AI agents in production. We'll be using langchain to use agents and create custom agents for Sofascore (a popular website for live statistics).

For now we'll be using Streamlit to generate the football facts. The goal is to evolve to a custom design.

The name of the project is an homage to my good friend Rui Tovar.

## Project setup

```bash
python -m venv env
source env/bin/activate
pip install -r requirements.txt
```

## Running the project

```bash
streamlit run main.py
```

Open in your browser in http://localhost:8501