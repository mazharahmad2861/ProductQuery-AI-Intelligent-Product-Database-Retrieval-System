from langgraph.graph import StateGraph
from app.state import GraphState
from app.agents.intent_agent import intent_agent
from app.agents.retrieval_agent import retrieval_agent
from app.agents.recommendation_agent import recommendation_agent
from app.agents.response_agent import response_agent

graph = StateGraph(GraphState)

graph.add_node("intent", intent_agent)
graph.add_node("retrieval", retrieval_agent)
graph.add_node("recommendation", recommendation_agent)
graph.add_node("response", response_agent)

graph.set_entry_point("intent")
graph.add_edge("intent", "retrieval")
graph.add_edge("retrieval", "recommendation")
graph.add_edge("recommendation", "response")

shopping_graph = graph.compile()
