from state import AgentState
from llm import ask_llm


def direct_answer_node(state: AgentState) -> AgentState:
    print("\n💡 Answering the question directly...")

    prompt = f"""
Answer the following question clearly and concisely.

Question: {state['topic']}

Provide a helpful, direct answer:
"""

    answer = ask_llm(prompt)

    # store the answer in both research and summary so the next node can use it
    return {**state, "research": answer, "summary": answer}
