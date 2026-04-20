from state import AgentState

MAX_ITERATIONS = 5


def react_edge(state: AgentState) -> str:
    action     = state.get("next_action", "done")
    iterations = state.get("react_iterations", 0)

    # stop if the agent says done OR the iteration limit is reached
    if action == "done" or iterations >= MAX_ITERATIONS:
        return "research"
    else:
        return "tool_executor"
