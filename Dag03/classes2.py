class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    def __repr__(self):
        return f'Point x: {self.x} & y: {self.y}'

class PointFactory:
    @staticmethod
    def CreatePoint(x, y):
        return Point(x,y)

p = Point(40, 61)
print(p)

p2 = PointFactory.CreatePoint(5,5)
print(p2)
