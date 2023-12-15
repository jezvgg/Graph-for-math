class verticle:
    def __init__(self, name, x, y):
        self.name = name
        self.x = x
        self.y = y

    def __str__(self):
        return f"{self.name} ({self.x}, {self.y})"

if __name__ == "__main__":
    p1 = verticle("A", 3, 4)
    print(p1)