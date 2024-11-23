from langchain_core.prompts import PromptTemplate
from langchain_community.chat_models import ChatOllama
from langchain_core.output_parsers import StrOutputParser
import time
from Third_Parties.linkedin import scrape_linkedin_profile
import os





if __name__=="__main__":
    print("Hello Langchain")

    summary_template="""
    given the linkedin information {information} about the person , I want you to create
    1. a short summary
    2. two interesting facts about them
    """
    summary_prompt_template=PromptTemplate(input_variables=["information"], template=summary_template)

    llm=ChatOllama(model="llama3.2") # The API key will be automatically loaded
    chain=summary_prompt_template|llm|StrOutputParser()
    linkedin_data=scrape_linkedin_profile(linkedin_profile_url="https://www.linkedin.com/in/raj-sanshi-5b97bb141/")
    res=chain.invoke(input={"information": linkedin_data})
    time.sleep(1)
    print(res)