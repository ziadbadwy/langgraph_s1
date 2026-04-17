from langgraph.graph import StateGraph, END

from state import AgentState, InputState

from nodes.input_node import input_node
from nodes.router_node import router_node
from nodes.clarify_node import clarify_node
from nodes.web_search_node import web_search_node
from nodes.research_node import research_node
from nodes.fact_check_node import fact_check_node
from nodes.summarize_node import summarize_node
from nodes.direct_answer_node import direct_answer_node
from nodes.draft_writer_node import draft_writer_node
from nodes.quality_check_node import quality_check_node
from nodes.revision_node import revision_node
from nodes.format_output_node import format_output_node

from edges.router_edge import router_edge
from edges.fact_check_edge import fact_check_edge
from edges.quality_edge import quality_edge


def build_graph():
    # input= tells Studio to only ask for InputState (topic only)
    graph = StateGraph(AgentState, input=InputState)

    # ── Add all nodes ──────────────────────────────────────────
    graph.add_node("input",          input_node)
    graph.add_node("router",         router_node)
    graph.add_node("clarify",        clarify_node)
    graph.add_node("web_search",     web_search_node)
    graph.add_node("research",       research_node)
    graph.add_node("fact_check",     fact_check_node)
    graph.add_node("summarize",      summarize_node)
    graph.add_node("direct_answer",  direct_answer_node)
    graph.add_node("draft_writer",   draft_writer_node)
    graph.add_node("quality_check",  quality_check_node)
    graph.add_node("revision",       revision_node)
    graph.add_node("format_output",  format_output_node)

    # ── Set the starting node ──────────────────────────────────
    graph.set_entry_point("input")

    # ── Regular edges (always go from A → B) ──────────────────
    graph.add_edge("input",          "router")
    graph.add_edge("web_search",     "research")
    graph.add_edge("research",       "fact_check")
    graph.add_edge("summarize",      "draft_writer")
    graph.add_edge("direct_answer",  "draft_writer")
    graph.add_edge("draft_writer",   "quality_check")
    graph.add_edge("revision",       "quality_check")
    graph.add_edge("format_output",  END)
    graph.add_edge("clarify",        END)

    # ── Conditional edges (choose next node based on state) ────
    graph.add_conditional_edges(
        "router",       # from this node...
        router_edge,    # ...call this function to decide where to go
        {
            "web_search":    "web_search",
            "direct_answer": "direct_answer",
            "clarify":       "clarify",
        }
    )

    graph.add_conditional_edges(
        "fact_check",
        fact_check_edge,
        {
            "research": "research",   # loop back if research score is low
            "summarize": "summarize",
        }
    )

    graph.add_conditional_edges(
        "quality_check",
        quality_edge,
        {
            "revision":      "revision",       # loop back if draft needs work
            "format_output": "format_output",
        }
    )

    return graph.compile()


# module-level graph for LangGraph Studio
graph = build_graph()
