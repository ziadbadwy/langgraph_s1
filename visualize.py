from graph import build_graph

app = build_graph()

# save the graph as a PNG image
png = app.get_graph().draw_mermaid_png()

with open("graph_v2.png", "wb") as f:
    f.write(png)

print("Graph saved to graph.png")
