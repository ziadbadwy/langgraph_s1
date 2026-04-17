from state import AgentState
from ddgs import DDGS


def web_search_node(state: AgentState) -> AgentState:
    print(f"\nSearching the web for: {state['topic']}")

    results = DDGS().text(state["topic"], max_results=5)

    # combine all results into one text block
    combined = ""
    for result in results:
        combined += f"Title: {result['title']}\n"
        combined += f"Summary: {result['body']}\n\n"

    print(f"   Found {len(results)} results.")
    return {**state, "search_results": combined}
