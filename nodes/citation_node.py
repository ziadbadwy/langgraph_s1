from state import AgentState
from llm import ask_llm


def citation_node(state: AgentState) -> AgentState:
    print("\nGenerating citations...")

    tools_log = "\n".join(state.get("tools_log", [])) or "No tools were used."

    prompt = f"""
Based on the research tools used below, write a clean "Sources" section
listing what was searched and what kind of sources were referenced.

Tools used:
{tools_log}

Write a short sources / references section:
"""

    citations = ask_llm(prompt)
    print("   Citations complete.")
    return {**state, "citations": citations}
