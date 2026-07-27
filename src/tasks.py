from crewai import Task
from agents import news_researcher, news_writer
from tools import search_tool

import yaml


# Load YAML configuration
with open("config/tasks.yaml", "r") as file:
    tasks_config = yaml.safe_load(file)


# Research Task
research_task = Task(
    config=tasks_config["research_task"],
    tools=[search_tool],
    agent=news_researcher
)


# Writing Task
write_task = Task(
    config=tasks_config["write_task"],
    tools=[search_tool],
    agent=news_writer,

    # Pass research output
    context=[research_task],

    output_file="outputs/output.md"
)