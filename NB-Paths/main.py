def isomorphic(graph1, graph2):
    if len(graph1) != len(graph2):
        return False
    visited = set()
    def dfs(v1, v2):
        if (v1, v2) in visited:
            return True
        visited.add((v1, v2))
        neighbors1 = graph1[v1]
        neighbors2 = graph2[v2]
        if len(neighbors1) != len(neighbors2):
            return False
        for n1, n2 in zip(neighbors1, neighbors2):
            if not dfs(n1, n2):
                return False
        return True
    for v1 in graph1:
        for v2 in graph2:
            visited.clear()
            if dfs(v1, v2):
                return True
    return False

graph1 = {
    'A': ['B', 'C'],
    'B': ['A', 'C'],
    'C': ['A', 'B']
}

graph2 = {
    'X': ['Y', 'Z'],
    'Y': ['X', 'Z'],
    'Z': ['X', 'Y']
}

if isomorphic(graph1, graph2):
    print("Графы изоморфны")
else:
    print("Графы неизоморфны")
