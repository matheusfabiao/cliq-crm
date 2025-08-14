import os

from dotenv import load_dotenv
from langchain import hub
from langchain.agents import AgentExecutor, create_react_agent
from langchain_google_genai import ChatGoogleGenerativeAI

from .tools import get_tools

load_dotenv(
    dotenv_path='secrets/.env',
)


def __get_llm():
    return ChatGoogleGenerativeAI(
        model=os.getenv('GOOGLE_AI_MODEL'),
        api_key=os.getenv('GOOGLE_API_KEY'),
    )


def __get_react_agent():
    return create_react_agent(
        llm=__get_llm(),
        tools=get_tools(),
        prompt=hub.pull('hwchase17/react'),
        stop_sequence=True,
    )


def get_agent_executor():
    return AgentExecutor.from_agent_and_tools(
        agent=__get_react_agent(),
        tools=get_tools(),
        verbose=True,
    )
