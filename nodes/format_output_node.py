from state import AgentState


def format_output_node(state: AgentState) -> AgentState:
    print("\nFormatting the final output...")

    # update conversation history with the current topic
    history = list(state.get("conversation_history") or [])
    history.append(state["topic"])

    tools_used = len(state.get("tools_log", []))

    final = f"""
{'=' * 60}
  TOPIC: {state['topic']}
{'=' * 60}

{state['draft']}

{'=' * 60}
  SOURCES
{'=' * 60}
{state.get('citations', 'N/A')}

{'=' * 60}
  EDITOR REFLECTION
{'=' * 60}
{state.get('reflection', 'N/A')}

{'=' * 60}
  STATS
  Research Quality Score : {state.get('fact_check_score', 'N/A')}/10
  Draft Quality Score    : {state.get('quality_score',    'N/A')}/10
  Revisions Made         : {state.get('revision_count',   0)}
  Tools Used             : {tools_used}
  Topics in this session : {len(history)}
{'=' * 60}
"""

    return {**state, "final_output": final, "conversation_history": history}
