from graph import build_graph


def main():
    print("\n" + "=" * 60)
    print("   Research & Writing Assistant  (powered by LangGraph)")
    print("=" * 60)

    topic = input("\nEnter your topic or question: ").strip()

    if not topic:
        print("No topic entered. Exiting.")
        return

    # build and compile the graph
    app = build_graph()

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

    print("\n🚀 Starting the workflow...\n")

    # run the graph from start to finish
    result = app.invoke(initial_state)

    # print the final result
    print(result["final_output"])


if __name__ == "__main__":
    main()
