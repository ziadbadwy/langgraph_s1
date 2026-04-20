from state import AgentState
from llm import ask_llm


def react_node(state: AgentState) -> AgentState:
    iterations = state.get("react_iterations", 0)
    print(f"\nReAct reasoning (iteration {iterations})...")

    tools_done = "\n".join(state.get("tools_log", [])) or "None yet"
    gathered   = state.get("gathered_info", "") or "Nothing gathered yet."

    prompt = f"""
You are a research agent. Your job is to gather information about the topic using tools.

Topic: {state['topic']}

Available tools:
- web_search  : search the internet for recent or general information
- wikipedia   : search Wikipedia for definitions and factual background
- calculator  : evaluate a math expression  (e.g. "15 * 24 / 2")
- get_date    : get today's date
- done        : stop gathering — you have enough information

Tools used so far:
{tools_done}

Information gathered so far:
{gathered[:1500]}

What should you do next?
Reply in this EXACT format (two lines only):
ACTION: <tool_name>
INPUT: <input or "none">
"""

    response = ask_llm(prompt).strip()

    action       = "done"
    action_input = ""

    for line in response.split("\n"):
        line = line.strip()
        if line.startswith("ACTION:"):
            action = line.replace("ACTION:", "").strip().lower()
        elif line.startswith("INPUT:"):
            action_input = line.replace("INPUT:", "").strip()

    valid = ["web_search", "wikipedia", "calculator", "get_date", "done"]
    if action not in valid:
        action = "done"

    print(f"   Decision: {action}({action_input})")
    return {**state, "next_action": action, "action_input": action_input}
