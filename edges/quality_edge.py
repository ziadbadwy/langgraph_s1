from state import AgentState


def quality_edge(state: AgentState) -> str:
    score = state.get("quality_score", 0)
    revision_count = state.get("revision_count", 0)

    # move forward if quality is good OR we already revised twice (to avoid infinite loop)
    if score >= 7 or revision_count >= 2:
        return "format_output"
    else:
        return "revision"
