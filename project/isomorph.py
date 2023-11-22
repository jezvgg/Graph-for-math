import numpy as np
from project.graph import Graph
from itertools import permutations


def isomorph_exp(goal_matrix: Graph, our_matrix: Graph) -> tuple[bool, Graph]:
    result = False, our_matrix
    for combo in permutations(range(len(our_matrix.verticles))):
        new_matrix = our_matrix.copy()
        new_matrix.set(list(combo))
        if goal_matrix == new_matrix:
            result = True, new_matrix
    return result


if __name__ == "__main__":
    result = isomorph_exp(goal_matrix=Graph({"A":"BCEF", "B":"ACDF", "C":"ABDE", "D":"BCEF", "E":"ACDF", "F":"ABDE"}),
    our_matrix=Graph({"A":"BCEF", "B":"ADEF", "C":"ADEF", "D":"BCEF", "E":"ABCD", "F":"ABCD"}))

    print(result[0])
    print(result[1])