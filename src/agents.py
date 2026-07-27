from crewai import Agent
from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI
from tools import search_tool

import yaml
import os

load_dotenv()


# Load YAML configuration
with open("config/agents.yaml", "r") as file:
    agents_config = yaml.safe_load(file)


# Gemini Model
llm = ChatGoogleGenerativeAI(
    model="gemini-2.5-flash",
    temperature=0.5,
    google_api_key=os.getenv("GEMINI_API_KEY")
)


# Research Agent
news_researcher = Agent(
    config=agents_config["researcher"],
    tools=[search_tool],
    llm=llm,
    verbose=True,
    memory=True,
    allow_delegation=True
)


# Writer Agent
news_writer = Agent(
    config=agents_config["writer"],
    tools=[search_tool],
    llm=llm,
    verbose=True,
    memory=True,
    allow_delegation=False
)