from state import AgentState
from llm import ask_llm


def router_node(state: AgentState) -> AgentState:
    print("\n🔀 Routing the topic...")

    prompt = f"""
You are a classifier. Read the topic below and classify it into one of these three categories:

- "research"  → the topic needs deep research and information gathering
- "simple"    → the topic can be answered directly without research
- "clarify"   → the topic is too vague or unclear to understand

Topic: {state['topic']}

Reply with ONLY one word: research, simple, or clarify
"""

    intent = ask_llm(prompt).strip().lower()

    # make sure the result is one of the valid options
    if intent not in ["research", "simple", "clarify"]:
        intent = "research"

    print(f"   Intent detected: {intent}")
    return {**state, "intent": intent}
