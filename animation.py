from project.graph import Graph
from project.verticle import verticle
from project.isomorph_evolve import isomorph_evolve
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from matplotlib.animation import PillowWriter
import numpy as np


def dot_space(fdot: verticle, tdot: verticle, n=24):
    x = np.linspace(fdot.x, tdot.x, n)
    y = np.linspace(fdot.y, tdot.y, n)
    return {'x':x,'y':y}


def frames(our: Graph, result: Graph, n=24) -> list[Graph]:
    frames = {}
    for dot in our.verticles:
        tdot = our.verticles[[i for i, vart in enumerate(result.verticles) if dot.name == vart.name][0]]
        frames[dot.name] = dot_space(dot, tdot, n)
    

    result = []
    for i in range(n):
        graph = our.copy()
        print(i, '='*10)
        for j,dot in enumerate(graph.verticles):
            dot.x = frames[dot.name]['x'][i]
            print(dot.x)
            dot.y = frames[dot.name]['y'][i]
            print(dot.y)
        result.append(graph)

    return result


if __name__=="__main__":
    goal_graph = Graph({"A":"BCEF", "B":"ACDF", "C":"ABDE", "D":"BCEF", "E":"ACDF", "F":"ABDE"})
    our_graph = Graph({"A":"BCEF", "B":"ADEF", "C":"ADEF", "D":"BCEF", "E":"ABCD", "F":"ABCD"})
    res_graph = isomorph_evolve(goal_matrix=goal_graph, our_matrix=our_graph)[1]

    print(our_graph.verticles)
    print(res_graph.verticles)

    fig = plt.figure()
    our_graph.plot(3.2,1)
    res_graph.plot(5.4,1)

    smezh = frames(our_graph, res_graph)

    def update(i):
        fig.clear()
        smezh[i].plot()
        res_graph.plot()

    anim = FuncAnimation(fig=fig, func=update, frames=24, interval=30, repeat=False)
    anim.save("simple_animation24.gif", dpi=300, writer=PillowWriter(fps=24))
    anim.save("simple_animation6.gif", dpi=300, writer=PillowWriter(fps=6))