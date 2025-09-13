from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
from agent.structure import *
from prompt import *
load_dotenv()

user_input = "Build a simple calculator app"



llm = ChatOpenAI(model = "gpt-4o-mini")

result = llm.with_structured_output(plan).invoke(prompt)
print(result)