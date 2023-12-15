import numpy as np
from project.verticle import verticle
import matplotlib.pyplot as plt


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


    def __eq__(self, __o: object) -> bool:
        return np.array_equal(self.matrix, __o.matrix)


    def __and__(self, __o: "Graph"):
        result = self.copy()
        result.matrix = (self.matrix+__o.matrix==2).astype(int)
        return result


    def __or__(self, __o: "Graph"):
        result = self.copy()
        result.matrix = (self.matrix+__o.matrix>0).astype(int)
        return result


    def __sub__(self, __o: "Graph"):
        result = self.copy()
        result.matrix = (self.matrix-__o.matrix>0).astype(int)
        return result


    def __xor__(self, __o: "Graph"):
        result = self.copy()
        result.matrix = (self.matrix!=__o.matrix).astype(int)
        return result


    def __str__(self):
        result = "  "+"".join(self.verticles)+"\n"
        for i,row in enumerate(self.matrix):
            result += self.verticles[i] + " " + "".join(map(str,row))+"\n"
        return result


    def __invert__(self):
        result = self.copy()
        result.matrix = (self.matrix==0).astype(int)
        return result


    def set(self, indexes: list[int]):
        '''
        Меняет вершины по заданым индексам.
        '''
        if len(indexes) != len(self.verticles):
            raise IndexError(f"indexes must be len of {len(self.verticles)}")

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


    def copy(self):
        return Graph(self.dict)


    def plot(self):
        if not isinstance(self.verticles, verticle):
            space = np.linspace(0, 2*np.pi, len(self.verticles))
            self.verticles = [verticle() for name, sp in zip(self.verticles, space)]



    @property
    def dict(self):
        review = {}
        for vert, row in zip(self.__verticles, self.matrix):
            review[vert] = ''.join([self.__verticles[i] for i,sym in enumerate(row) if sym])
        return review


    @property
    def verticles(self):
        return self.__verticles


    @verticles.setter
    def verticles(self, verts):
        verts = list(verts.keys())
        if isinstance(verts[0], verticle):
            self.__verticles = [x.name for x in verts]
        else:
            self.__verticles = verts


if __name__ == "__main__":
    g = Graph({'a':'ad','b':'ad','c':'bc','d':'bc'})
    h=Graph({'a':'bd','b':'bc','c':'bc','d':'ac'})
    print("graph G1:",g,sep="\n")
    print("graph H1:",h,sep="\n")
    print("graph G1 and H1:",g&h,sep="\n")
    print("graph G1 or H1:",g|h,sep="\n")
    print("graph G1 / H1:",g-h,sep="\n")
    print("graph G1 xor H1:",g^h,sep="\n")
    print("Invert G1:",~g)
    
    