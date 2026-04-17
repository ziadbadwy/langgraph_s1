from state import AgentState
from llm import ask_llm


def research_node(state: AgentState) -> AgentState:
    print("\n📚 Writing research based on search results...")

    prompt = f"""
You are a researcher. Use the search results below to write a detailed research summary about the topic.

Topic: {state['topic']}

Search Results:
{state.get('search_results', 'No search results available.')}

Write a clear and detailed research summary:
"""

    research = ask_llm(prompt)
    print("   Research complete.")
    return {**state, "research": research}
