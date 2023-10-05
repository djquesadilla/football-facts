import os

import openai
import streamlit as st
from dotenv import load_dotenv
from langchain.agents import AgentType, initialize_agent, load_tools
from langchain.chat_models import ChatOpenAI

load_dotenv()

openai.api_key = os.getenv('OPENAI_API_KEY')
SERPAPI_API_KEY = os.getenv('SERPAPI_API_KEY')

llm = ChatOpenAI(
    temperature=0.7, max_tokens=900,
    max_retries=6, model_name="gpt-4",
    streaming=True, verbose=True
)

def submit(question):
    tools = load_tools(["serpapi"], llm=llm)

    agent = initialize_agent(tools, llm, agent=AgentType.ZERO_SHOT_REACT_DESCRIPTION, verbose=True)

    output = agent.run(question)

    return output


def main():
    st.title("Ask fun football facts with AI")
    
    # Create a list of examples for the user to choose from
    examples = [
        "Who sponsored Arsenal kits in 1998?",
        "What English player played for three teams in the same season?",
        "Which goalkeeper scored a goal from his own penalty area in a professional match?",
        "Which football club holds the record for the longest unbeaten streak in domestic league matches?",
    ]

    # Create a selectbox for the user to choose from the examples
    user_input = st.selectbox("Choose an example", examples)

    # Create a submit button
    if st.button("Submit"):
        st.write(submit(question=user_input))

if __name__ == "__main__":
    main()