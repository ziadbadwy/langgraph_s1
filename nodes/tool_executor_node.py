from state import AgentState
from tools import TOOLS


def tool_executor_node(state: AgentState) -> AgentState:
    action       = state.get("next_action", "done")
    action_input = state.get("action_input", "")
    iterations   = state.get("react_iterations", 0) + 1

    print(f"\nExecuting tool [{iterations}]: {action}({action_input})")

    tool_fn = TOOLS.get(action)
    if tool_fn:
        result = tool_fn() if action == "get_date" else tool_fn(action_input)
    else:
        result = "Unknown tool."

    # append to the tools log
    log_entry = f"[{action}] {action_input} → {result[:150]}"
    tools_log = state.get("tools_log", []) + [log_entry]

    # append to gathered info
    gathered  = state.get("gathered_info", "")
    gathered += f"\n\n--- {action}: {action_input} ---\n{result}"

    print(f"   Result preview: {result[:80]}...")

    return {
        **state,
        "tool_result":      result,
        "react_iterations": iterations,
        "tools_log":        tools_log,
        "gathered_info":    gathered,
    }
