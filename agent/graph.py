from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
from structure import *
from prompt import *
load_dotenv()

user_input = "Build a simple calculator app"

llm = ChatOpenAI(model = "gpt-4o-mini")

def planner_agent(state: dict)-> dict:
    user_input = state["user_input"]
    result = llm.with_structured_output(plan).invoke(prompt(user_input))
    return {"plan":result}

