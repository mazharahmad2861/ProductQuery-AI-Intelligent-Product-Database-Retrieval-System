def recommendation_agent(state):
    if state.intent == "compare":
        state.ranked_items = state.retrieved_items
        return state

    ranked = sorted(
        state.retrieved_items,
        key=lambda x: (x["rating"], -x["price"]),
        reverse=True
    )

    state.ranked_items = ranked[:5]
    return state
