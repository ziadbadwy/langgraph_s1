from typing import TypedDict, List


class InputState(TypedDict):
    topic: str


class AgentState(TypedDict):
    topic: str
    intent: str               # "research", "simple", "clarify"

    # ── ReAct ──────────────────────────────────────────────────
    next_action: str          # "web_search", "wikipedia", "calculator", "get_date", "done"
    action_input: str         # input for the current tool
    tool_result: str          # result from the last tool call
    react_iterations: int     # how many times the ReAct loop has run
    tools_log: List[str]      # history of all tool calls
    gathered_info: str        # all information collected across tool calls
    search_queries: List[str] # planned queries from query_planner

    # ── Research ───────────────────────────────────────────────
    search_results: str
    research: str
    critique: str             # critical analysis of the research
    fact_check_score: int     # score from 1 to 10

    # ── Writing ────────────────────────────────────────────────
    summary: str
    draft: str
    citations: str            # sources section
    quality_score: int        # score from 1 to 10
    revision_count: int
    reflection: str           # editor reflection on the final output

    # ── Memory ─────────────────────────────────────────────────
    conversation_history: List[str]  # list of past topics in this session

    # ── Output ─────────────────────────────────────────────────
    final_output: str
