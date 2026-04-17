from state import AgentState


def input_node(state: AgentState) -> AgentState:
    print(f"\n📥 Topic received: {state['topic']}")

    # fill in default values for all other fields
    return {
        "topic":            state["topic"],
        "intent":           "",
        "search_results":   "",
        "research":         "",
        "fact_check_score": 0,
        "summary":          "",
        "draft":            "",
        "quality_score":    0,
        "revision_count":   0,
        "final_output":     "",
    }
