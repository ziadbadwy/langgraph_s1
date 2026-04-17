import gradio as gr
from graph import build_graph

# build the graph once when the app starts
app = build_graph()


def run_agent(topic: str) -> str:
    # define the starting state
    initial_state = {
        "topic":            topic,
        "intent":           "",
        "search_results":   "",
        "research":         "",
        "fact_check_score": 0,
        "summary":          "",
        "draft":            "",
        "quality_score":    0,
        "revision_count":   0,
        "final_output":     "",
    }

    # run the full graph
    result = app.invoke(initial_state)

    return result["final_output"]


def respond(message, chat_history):
    return run_agent(message)


gr.ChatInterface(
    fn=respond,
    title="Research & Writing Assistant — powered by LangGraph",
    description="Ask any question or give a topic. The agent will search the web, research it, write a draft, and deliver a polished article.",
    examples=[
        "What is quantum computing and how does it work?",
        "What are the latest developments in AI in 2024?",
        "What is the capital of France?",
        "What is the impact of climate change on ocean life?",
        "How do large language models like GPT work?",
    ],
).launch()
