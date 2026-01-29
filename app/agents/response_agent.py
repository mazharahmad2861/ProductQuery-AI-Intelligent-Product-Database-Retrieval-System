def response_agent(state):
    if state.intent == "compare":
        state.response = {
            "mode": "comparison",
            "products": state.ranked_items
        }
    else:
        state.response = {
            "mode": "list",
            "results": state.ranked_items
        }

    return state
