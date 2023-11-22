import numpy as np
from project.graph import Graph
from itertools import permutations


def isomorph_exp(goal_matrix: Graph, our_matrix: Graph) -> tuple[bool, Graph]:
    for combo in permutations(range(6)):
        new_matrix = our_matrix.copy()
        new_matrix.set(list(combo))
        if goal_matrix == new_matrix:
            return True, new_matrix
    else:
        return False, our_matrix


if __name__ == "__main__":
    result = isomorph_exp(goal_matrix=Graph({"A":"BCEF", "B":"ACDF", "C":"ABDE", "D":"BCEF", "E":"ACDF", "F":"ABDE"}),
    our_matrix=Graph({"A":"BCEF", "B":"ADEF", "C":"ADEF", "D":"BCEF", "E":"ABCD", "F":"ABCD"}))

    print(result[0])
    print(result[1])