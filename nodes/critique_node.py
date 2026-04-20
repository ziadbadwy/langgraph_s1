from state import AgentState
from llm import ask_llm


def critique_node(state: AgentState) -> AgentState:
    print("\nCritiquing the research...")

    prompt = f"""
You are a critical analyst. Read the research below and write a short critique.
Focus on:
- What important information might be missing?
- Are there any potential biases or gaps?
- What should the writer pay attention to?

Topic: {state['topic']}

Research:
{state['research']}

Write a short critique (3-5 bullet points):
"""

    critique = ask_llm(prompt)
    print("   Critique complete.")
    return {**state, "critique": critique}
