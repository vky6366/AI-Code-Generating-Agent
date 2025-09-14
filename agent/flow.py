from langgraph.graph import StateGraph
from .graph import *


my_graph = StateGraph(dict)

my_graph.add_node("planner", planner_agent)
my_graph.add_node("architect", architect_agent)
my_graph.add_node("coder", coder_agent)

my_graph.add_edge("planner", "architect")
my_graph.add_edge("architect", "coder")
my_graph.add_conditional_edges(
    "coder",
    lambda s: "END" if s.get("status") == "DONE" else "coder",
    {"END": END, "coder": "coder"}
)

my_graph.set_entry_point("planner")
agent = my_graph.compile()
if __name__ == "__main__":
    result = agent.invoke({"user_prompt": "Build a colourful modern todo app in html css and js"},
                          {"recursion_limit": 100})
    print("Final State:", result)