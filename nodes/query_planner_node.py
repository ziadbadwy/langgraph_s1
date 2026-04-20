from state import AgentState
from llm import ask_llm


def query_planner_node(state: AgentState) -> AgentState:
    print("\nPlanning research strategy...")

    prompt = f"""
You are a research planner. Given the topic below, write 2-3 specific search queries
that will help gather comprehensive and accurate information.

Topic: {state['topic']}

Reply with ONLY a numbered list of queries:
1. first query
2. second query
3. third query
"""

    response = ask_llm(prompt)

    queries = []
    for line in response.strip().split("\n"):
        line = line.strip()
        if line and line[0].isdigit():
            query = line.split(".", 1)[-1].strip()
            if query:
                queries.append(query)

    if not queries:
        queries = [state["topic"]]

    print(f"   Planned {len(queries)} queries.")

    return {
        **state,
        "search_queries":   queries,
        "next_action":      "web_search",
        "action_input":     queries[0],
        "react_iterations": 0,
        "tools_log":        [],
        "gathered_info":    "",
    }
