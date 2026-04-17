from state import AgentState
from llm import ask_llm


def draft_writer_node(state: AgentState) -> AgentState:
    print("\n✍️  Writing the draft article...")

    # use summary if available, otherwise fall back to raw research
    content = state.get("summary") or state.get("research", "")

    prompt = f"""
You are a writer. Using the research summary below, write a well-structured article about the topic.
Include an introduction, main points, and a conclusion.

Topic: {state['topic']}

Research Summary:
{content}

Write the full article:
"""

    draft = ask_llm(prompt)
    print("   Draft complete.")
    return {**state, "draft": draft}
