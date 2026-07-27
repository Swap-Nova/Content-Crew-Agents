from dotenv import load_dotenv
from crewai_tools import SerperDevTool
import os

# Load environment variables
load_dotenv()

# Retrieve API key
serper_api_key = os.getenv("SERPER_API_KEY")

if not serper_api_key:
    raise ValueError("SERPER_API_KEY is not set in the environment variables.")

# Initialize Serper search tool
search_tool = SerperDevTool()