import os

import openai
import streamlit as st
from dotenv import load_dotenv
from langchain.agents import AgentType, initialize_agent, load_tools
from langchain.chat_models import ChatOpenAI
from langchain.tools import DuckDuckGoSearchRun, Tool

load_dotenv()

openai.api_key = os.getenv('OPENAI_API_KEY')


search = DuckDuckGoSearchRun()

duckduckgo_tool = Tool(
    name="duckduckgo",
    func=search.run,
    description="Useful for when you need to do a search on the internet to find information."
)

tools = [duckduckgo_tool]

llm = ChatOpenAI(
    temperature=0.7, max_tokens=900,
    max_retries=6, model_name="gpt-4",
    streaming=True, verbose=True
)

finding_facts_prompt = """
You are an AI assistant that helps people find facts about football.
You will be given 2 teams that are playing against each other at the moment.
You will need to find three facts about the teams and the match. I want these facts to be between the most obvious and the most obscure facts.

Some funny facts are:
- Who sponsored Arsenal kits in 1998?
- What English player played for three teams in the same season?
- Which goalkeeper scored a goal from his own penalty area in a professional match?
- Which football club holds the record for the longest unbeaten streak in domestic league matches?

I want you to be funny and sarcastic on these comments kind of facts that you want to find.

I want you to reply with 3 facts that you want to find and only the facts that you want to find.

The teams are {team_1} and {team_2}.
"""

def submit(question):
    agent = initialize_agent(
        tools,
        llm,
        agent=AgentType.ZERO_SHOT_REACT_DESCRIPTION,
        verbose=True
    )

    output = agent.run(question)

    return output


def main():
    st.title("Tovar AI - Ask for football facts")

    team_1 = st.text_input("Team 1", "Arsenal")
    team_2 = st.text_input("Team 2", "Chelsea")

    # Create a submit button
    if st.button("Submit"):
        st.write(submit(question=finding_facts_prompt.format(team_1=team_1, team_2=team_2)))

if __name__ == "__main__":
    main()