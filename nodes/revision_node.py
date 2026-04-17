from state import AgentState
from llm import ask_llm


def revision_node(state: AgentState) -> AgentState:
    count = state.get("revision_count", 0) + 1
    print(f"\n🔄 Revising the draft (revision #{count})...")

    prompt = f"""
You are an editor. Improve the draft below.
Make it clearer, more detailed, and better structured.

Topic: {state['topic']}

Current Draft:
{state['draft']}

Write an improved version:
"""

    revised_draft = ask_llm(prompt)
    print("   Revision complete.")
    return {**state, "draft": revised_draft, "revision_count": count}
