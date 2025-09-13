from langgraph.graph import StateGraph
from graph import *


mygraph = StateGraph(dict)
mygraph.add_node("planner", planner_agent)
mygraph.set_entry_point("planner")

agent = mygraph.compile()

user_input = "Create a simple calculator"

result = agent.invoke({'user_input': user_input})

print(result)