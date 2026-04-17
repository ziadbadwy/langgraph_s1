from state import AgentState


def clarify_node(state: AgentState) -> AgentState:
    print("\nThe topic is too vague. Asking for clarification...")

    message = "Your topic is unclear. Please provide more details and try again."
    return {**state, "final_output": message}
