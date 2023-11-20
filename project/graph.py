import numpy as np
from verticle import verticle

class Graph:
    '''
    Graph by matrix
    '''

    __verticles = []
    __edges = []
    matrix = []

    def __init__(self, verticles: dict[str|verticle]):
        self.verticles = verticles
        matrix = []
        for vert in self.verticles:
            to = verticles[vert]
            matrix.append( [1 if x in to else 0 for x in self.verticles] )
        self.matrix = np.array(matrix)


    def __str__(self):
        result = "  "+"".join(self.verticles)+"\n"
        for i,row in enumerate(self.matrix):
            result += self.verticles[i] + " " + "".join(map(str,row))+"\n"
        return result


    def set(self, indexes: list):
        '''
        Меняет вершины по заданым индексам.
        '''
        new_matrix = self.matrix[indexes]
        self.matrix = new_matrix[:, indexes]
        self.__verticles = [self.verticles[x] for x in indexes]


    def replace(self, fro:str|verticle, to:str|verticle):
        '''
        Меняет 2 переданные вершины графа местами.
        '''
        index_fro = self.verticles.index(str(fro))
        index_to = self.verticles.index(str(to))
        indexes = [index_to if i==index_fro else index_fro if i==index_to else i for i in range(len(self.verticles))]
        self.set(indexes)


    @property
    def verticles(self):
        return self.__verticles


    @verticles.setter
    def verticles(self, verts: dict[str|verticle]):
        verts = list(verts.keys())
        if isinstance(verts[0], verticle):
            self.__verticles = [x.name for x in verts]
        else:
            self.__verticles = verts


if __name__ == "__main__":
    g = Graph({"A":"BC", "B":"ABC", "C":"AB"})
    print(g)
    g.replace("A","B")
    print(g)
    g.set([0,2,1])
    print(g)