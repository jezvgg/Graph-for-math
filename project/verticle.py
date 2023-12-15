import math
import matplotlib.pyplot as plt

class verticle:
    def __init__(self, name, x=None, y=None):
        self.name = name
        self.x = x
        self.y = y

    def __str__(self):
        if self.x is not None and self.y is not None:
            return f"{self.name} ({self.x}, {self.y})"
        else:
            return self.name

    def plot_on_cartesian(self):
        if self.x is None or self.y is None:
            print("Координаты не заданы.")
        else:
            print(f"Точка {self.name} с координатами ({self.x}, {self.y}).")
            plt.scatter(self.x, self.y, color='blue')
            plt.text(self.x, self.y, self.name)
            plt.xlabel("X")
            plt.ylabel("Y")
            plt.title("Точки на декартовой системе координат")
            plt.grid(True)

if __name__ == "__main__":
    p1 = verticle("A", 3, 4)
    p1.plot_on_cartesian()