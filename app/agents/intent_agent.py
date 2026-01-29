def intent_agent(state):
    query = state.user_query.lower()

    if "compare" in query:
        state.intent = "compare"
    elif "recommend" in query or "best" in query:
        state.intent = "recommend"
    elif "under" in query or "below" in query:
        state.intent = "filter"
    else:
        state.intent = "search"

    return state
