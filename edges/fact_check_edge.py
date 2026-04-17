from state import AgentState


def fact_check_edge(state: AgentState) -> str:
    score = state.get("fact_check_score", 0)

    # if the research quality is low, go back and redo the research
    if score < 6:
        return "research"
    else:
        return "summarize"
