from state import AgentState


def router_edge(state: AgentState) -> str:
    intent = state.get("intent", "research")

    if intent == "simple":
        return "direct_answer"
    elif intent == "clarify":
        return "clarify"
    else:
        return "web_search"
