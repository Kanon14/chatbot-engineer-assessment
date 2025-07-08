from agent.workflow import GraphBuilder

# Initialize the chatbot graph
builder = GraphBuilder(model_provider="openai")
chatbot_graph = builder()

# Run test conversation
if __name__ == "__main__":
    print("ZUS Coffee Chatbot is ready. Ask your question:")
    while True:
        query = input("User: ")
        if query.lower() in ["exit", "quit"]:
            print("Goodbye!")
            break

        state = {"messages": [{"role": "user", "content": query}]}
        result = chatbot_graph.invoke(state)
        response = result["messages"][-1].content
        print("Bot:", response)
