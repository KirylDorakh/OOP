class Point:
    def __init__(self, x, y, z):
        self.coord = (x, y, z)


p = Point(1, 2, 3)
print(p.coord)
print(p.__dict__)
