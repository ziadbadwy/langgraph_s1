import uuid
from graph import build_graph


def main():
    print("\n" + "=" * 60)
    print("   Research & Writing Assistant  (powered by LangGraph)")
    print("=" * 60)

    print("\nEnter a session ID to continue a previous conversation,")
    session_id = input("or press Enter to start a new session: ").strip()

    if not session_id:
        session_id = str(uuid.uuid4())
        print(f"New session started: {session_id}")
    else:
        print(f"Resuming session: {session_id}")

    config = {"configurable": {"thread_id": session_id}}
    app    = build_graph()

    while True:
        print("\n" + "-" * 60)
        topic = input("Enter your topic (or 'exit' to quit): ").strip()

        if topic.lower() == "exit":
            print("Goodbye!")
            break

        if not topic:
            continue

        print("\nStarting the workflow...\n")
        result = app.invoke({"topic": topic}, config=config)
        print(result["final_output"])


if __name__ == "__main__":
    main()
