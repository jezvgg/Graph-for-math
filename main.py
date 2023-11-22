from project.graph import Graph
from project.isomorph_evolve import isomorph_evolve
from project.isomorph import isomorph_exp
from datetime import datetime
from random import sample

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

# Test 3
goal_graph = Graph({"a":"bfi", "b":"ach", "c":"bdg", "d":"cei", "e":"dfh", "f":"aeg", "g":"cfj", "h":"bej", "i":"adj", "j":"ghi"})
our_graph = Graph({"a":"bef", "b":"acg","c":"bdh", "d":"cei", "e":"adj", "f":"ahi", "g":"bij", "h":"cfj", "i":"dfg", "j":"egh"})

start_time = datetime.now()
print(isomorph_exp(goal_matrix=goal_graph, our_matrix=our_graph))
print(datetime.now() - start_time)

start_time = datetime.now()
print(isomorph_evolve(goal_matrix=goal_graph, our_matrix=our_graph))
print(datetime.now() - start_time)

# Test 4
goal_graph = Graph({"a":"hijk", "b":"i", "c":"i", "d":"jk", "e":"jk", "f":"jk", "g":"k", "h":"ajk","i":"abck","j":"adefhk", "k":"adefghij"})
our_graph = goal_graph.copy()
our_graph.set(sample(range(11), k=11))

start_time = datetime.now()
print(isomorph_exp(goal_matrix=goal_graph, our_matrix=our_graph))
print(datetime.now() - start_time)

start_time = datetime.now()
print(isomorph_evolve(goal_matrix=goal_graph, our_matrix=our_graph))
print(datetime.now() - start_time)