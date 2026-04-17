from typing import TypedDict


class InputState(TypedDict):
    topic: str


class AgentState(TypedDict):
    topic: str
    intent: str            # "research", "simple", or "clarify"
    search_results: str
    research: str
    fact_check_score: int  # score from 1 to 10
    summary: str
    draft: str
    quality_score: int     # score from 1 to 10
    revision_count: int
    final_output: str
