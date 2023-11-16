import networkx as nx
import matplotlib.pyplot as plt

def is_isomorphic(graph1, graph2):
    return nx.is_isomorphic(graph1, graph2)

def print_graph(graph):
    pos = nx.spring_layout(graph)
    nx.draw_networkx_nodes(graph, pos, node_size=200)
    nx.draw_networkx_edges(graph, pos)
    nx.draw_networkx_labels(graph, pos, font_size=10)
    plt.axis("off")
    plt.show()

graph1 = nx.Graph()
graph1.add_edges_from([("A", "B"), ("A", "C"), ("B", "C"), ("A", "E"), ("E", "K")])

graph2 = nx.Graph()
graph2.add_edges_from([("X", "Y"), ("X", "Z"), ("Y", "Z")])

if is_isomorphic(graph1, graph2):
    print("Графы изоморфны")
else:
    print("Графы не изоморфны")

print_graph(graph1)

print_graph(graph2)