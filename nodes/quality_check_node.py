from state import AgentState
from llm import ask_llm


def quality_check_node(state: AgentState) -> AgentState:
    print("\nChecking the draft quality...")

    prompt = f"""
You are an editor. Read the draft below and give it a quality score from 1 to 10.

Scoring guide:
- 1  = very poor (unclear, incomplete, or badly written)
- 10 = excellent (clear, detailed, and well-structured)

Draft:
{state['draft']}

Reply with ONLY a number from 1 to 10.
"""

    score_text = ask_llm(prompt).strip()

    # safely extract the number from the response
    try:
        score = int("".join(filter(str.isdigit, score_text[:3])))
        score = max(1, min(10, score))  # keep it between 1 and 10
    except Exception:
        score = 5

    print(f"   Quality score: {score}/10")
    return {**state, "quality_score": score}
