from state import AgentState


def input_node(state: AgentState) -> AgentState:
    print(f"\nTopic received: {state['topic']}")

    # preserve conversation history from previous sessions (memory)
    history = list(state.get("conversation_history") or [])

    return {
        "topic":                state["topic"],
        "intent":               "",
        "next_action":          "",
        "action_input":         "",
        "tool_result":          "",
        "react_iterations":     0,
        "tools_log":            [],
        "gathered_info":        "",
        "search_queries":       [],
        "search_results":       "",
        "research":             "",
        "critique":             "",
        "fact_check_score":     0,
        "summary":              "",
        "draft":                "",
        "citations":            "",
        "quality_score":        0,
        "revision_count":       0,
        "reflection":           "",
        "conversation_history": history,
        "final_output":         "",
    }
