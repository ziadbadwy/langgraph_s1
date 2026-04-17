from state import AgentState
from llm import ask_llm


def fact_check_node(state: AgentState) -> AgentState:
    print("\nFact checking the research...")

    prompt = f"""
You are a fact checker. Read the research below and give it a quality score from 1 to 10.

Scoring guide:
- 1  = very poor (too short, unreliable, or off-topic)
- 10 = excellent (detailed, accurate, and trustworthy)

Research:
{state['research']}

Reply with ONLY a number from 1 to 10.
"""

    score_text = ask_llm(prompt).strip()

    # safely extract the number from the response
    try:
        score = int("".join(filter(str.isdigit, score_text[:3])))
        score = max(1, min(10, score))  # keep it between 1 and 10
    except Exception:
        score = 5

    print(f"   Fact check score: {score}/10")
    return {**state, "fact_check_score": score}
