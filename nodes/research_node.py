from state import AgentState
from llm import ask_llm


def research_node(state: AgentState) -> AgentState:
    print("\nSynthesizing research from gathered information...")

    # use ReAct-gathered info if available, fallback to raw search results
    content = state.get("gathered_info") or state.get("search_results", "No information available.")

    prompt = f"""
        You are a researcher. Using all the information gathered below, write a detailed research summary about the topic.

        Topic: {state['topic']}

        Gathered Information:
        {content}

        Write a clear and detailed research summary:
        """

    research = ask_llm(prompt)
    print("Research complete.")
    return {**state, "research": research}
