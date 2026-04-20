import uuid
import gradio as gr
from graph import build_graph

app_graph = build_graph()


def chat(message, history, session_id):
    # create a new session ID if this is the first message
    if not session_id:
        session_id = str(uuid.uuid4())

    config = {"configurable": {"thread_id": session_id}}
    result = app_graph.invoke({"topic": message}, config=config)
    output = result["final_output"]

    history.append((message, output))
    return history, "", session_id


with gr.Blocks() as demo:
    gr.Markdown("# Research & Writing Assistant — powered by LangGraph")
    gr.Markdown(
        "Ask any question or give a topic. "
        "The agent will plan queries, search the web, research, write a draft, and deliver a polished article."
    )

    session_state = gr.State(None)

    chatbot   = gr.Chatbot(height=500)
    msg_input = gr.Textbox(
        label="Your topic or question",
        placeholder="e.g. What is quantum computing?",
    )

    gr.Examples(
        examples=[
            "What is quantum computing and how does it work?",
            "What are the latest developments in AI in 2024?",
            "What is the capital of France?",
            "What is the impact of climate change on ocean life?",
            "How do large language models like GPT work?",
        ],
        inputs=msg_input,
    )

    msg_input.submit(
        chat,
        inputs=[msg_input, chatbot, session_state],
        outputs=[chatbot, msg_input, session_state],
    )

    gr.Button("Send").click(
        chat,
        inputs=[msg_input, chatbot, session_state],
        outputs=[chatbot, msg_input, session_state],
    )

demo.launch()
