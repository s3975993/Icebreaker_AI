from langchain_community.tools.tavily_search import TavilySearchResults
import os
from dotenv import load_dotenv

def get_profile_url_tavily(name:str):
    load_dotenv()
    search=TavilySearchResults()
    res=search.run(f"{name}")
    return res