from state import AgentState


def format_output_node(state: AgentState) -> AgentState:
    print("\n🎨 Formatting the final output...")

    final = f"""
{'=' * 60}
  TOPIC: {state['topic']}
{'=' * 60}

{state['draft']}

{'=' * 60}
  Research Quality Score : {state.get('fact_check_score', 'N/A')}/10
  Draft Quality Score    : {state.get('quality_score',    'N/A')}/10
  Revisions Made         : {state.get('revision_count',   0)}
{'=' * 60}
"""

    return {**state, "final_output": final}
