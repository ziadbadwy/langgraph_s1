from state import AgentState
from llm import ask_llm


def reflection_node(state: AgentState) -> AgentState:
    print("\nReflecting on the final output...")

    prompt = f"""
You are a senior editor. Write a 2-3 sentence reflection on this article.
Mention its strengths and any remaining areas for improvement.

Topic: {state['topic']}

Draft:
{state['draft'][:800]}

Critique received during research:
{state.get('critique', 'None')}

Write your reflection:
"""

    reflection = ask_llm(prompt)
    print("   Reflection complete.")
    return {**state, "reflection": reflection}
