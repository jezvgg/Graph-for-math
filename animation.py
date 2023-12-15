from project.graph import Graph
from project.isomorph_evolve import isomorph_evolve
import matplotlib.pyplot as plt

goal_graph = Graph({"A":"BCEF", "B":"ACDF", "C":"ABDE", "D":"BCEF", "E":"ACDF", "F":"ABDE"})
our_graph = Graph({"A":"BCEF", "B":"ADEF", "C":"ADEF", "D":"BCEF", "E":"ABCD", "F":"ABCD"})

goal_graph.plot(1,1)
our_graph.plot(3.2,1)

# res_graph = isomorph_evolve(goal_matrix=goal_graph, our_matrix=our_graph)[1]

# res_graph.plot(3.2, 1)

plt.show()