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

# Test 2
goal_graph = Graph({"1":"245", "2":"136", "3":"247", "4":"138", "5":"168", "6":"257", "7":"368", "8":"457"})
our_graph = Graph({"a":"ghi", "b":"ghj", "c":"gij", "d":"hij", "g":"abc", "h":"abd", "i":"acd", "j":"bcd"})

start_time = datetime.now()
print(isomorph_exp(goal_matrix=goal_graph, our_matrix=our_graph))
print(datetime.now() - start_time)

start_time = datetime.now()
print(isomorph_evolve(goal_matrix=goal_graph, our_matrix=our_graph))
print(datetime.now() - start_time)