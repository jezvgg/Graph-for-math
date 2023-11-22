from project.graph import Graph
from project.isomorph_evolve import isomorph_evolve
from project.isomorph import isomorph_exp
from datetime import datetime

# Test 1
goal_graph = Graph({"A":"BCEF", "B":"ACDF", "C":"ABDE", "D":"BCEF", "E":"ACDF", "F":"ABDE"})
our_graph = Graph({"A":"BCEF", "B":"ADEF", "C":"ADEF", "D":"BCEF", "E":"ABCD", "F":"ABCD"})

start_time = datetime.now()
print(isomorph_exp(goal_matrix=goal_graph, our_matrix=our_graph))
print(datetime.now() - start_time)

start_time = datetime.now()
print(isomorph_evolve(goal_matrix=goal_graph, our_matrix=our_graph))
print(datetime.now() - start_time)

