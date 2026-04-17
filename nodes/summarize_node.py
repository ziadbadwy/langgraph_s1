from state import AgentState
from llm import ask_llm


def summarize_node(state: AgentState) -> AgentState:
    print("\nSummarizing the research...")

    prompt = f"""
Summarize the following research into clear bullet points.
Keep the most important facts and remove unnecessary details.

Research:
{state['research']}

Write a clean bullet-point summary:
"""

    summary = ask_llm(prompt)
    print("   Summary complete.")
    return {**state, "summary": summary}
