import os
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from langchain.prompts.prompt import PromptTemplate
from langchain_core.tools import Tool
from langchain.agents import (
    create_react_agent,
    AgentExecutor,
)
from langchain import hub



def lookup(name:str)->str:
   llm=ChatOpenAI(temperature=0,model_name="gpt-40-mini",)
   
   template="""Given the full name {name_of_the_person} of the person. I want you to give me the link to their linkedin profile
    Your answer should only be a URL.
   """
   
   prompt_template=PromptTemplate(template=template,input_varaiables=["name_of_the_person"])
   
   tools_for_agent = [
       Tool(
           name="Crawl google for linkedin page"
           func="?"
           description="Useful when you need to get the Linkedin Page URL",
       )
   ]
   
   react_prompt=hub.pull("hwchase17/react")
   agent=create_react_agent(llm=llm,tools=tools_for_agent,prompt=react_prompt)
   agent_executor = AgentExecutor(agent=agent, tools=tools_for_agent, verbose=True)

   result = agent_executor.invoke(
        input={"input": prompt_template.format_prompt(name_of_person=name)}
    )

   linked_profile_url = result["output"]
   return linked_profile_url

if __name__ == "__main__":
    print(lookup(name="Raj Sanshi CSIRO"))