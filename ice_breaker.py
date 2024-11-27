from langchain_core.prompts import PromptTemplate
from langchain_community.chat_models import ChatOllama
from langchain_core.output_parsers import StrOutputParser
import time
from Third_Parties.linkedin import scrape_linkedin_profile
import os
from dotenv import load_dotenv
from Agents.linkedin_lookup_agent import lookup as linkedin_lookup_agent
from output_parser import summary_parser, Summary
from typing import Tuple


def ice_break_with(name:str)->Tuple[Summary, str]:
    #linkedin URL
    linkedin_username=linkedin_lookup_agent(name=name)
    linkedin_data=scrape_linkedin_profile(linkedin_profile_url=linkedin_username,mock=True)
    
    summary_template="""
    given the linkedin information {information} about the person , I want you to create
    1. a short summary
    2. two interesting facts about them
    
    \n{format_instructions}
    """
    summary_prompt_template=PromptTemplate(
        input_variables=["information"], template=summary_template,
         partial_variables={"format_instructions":summary_parser.get})

    llm=ChatOllama(model="llama3.2") # The API key will be automatically loaded
    chain=summary_prompt_template|llm|summary_parser
    res:Summary=chain.invoke(input={"information": linkedin_data})
    return res, linkedin_data.get("profile_pic_url")

if __name__=="__main__":
    load_dotenv()
    print("Ice Break Enter")
    ice_break_with(name="Eden Marco Udemy linkedin")
    

    