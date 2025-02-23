class Point:
    # constructor is a value that gets called at the point of initializing the object

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def move(self):
        print("move")

    def draw(self):
        print("draw")

point = Point(10, 20)
point.x = 11
print(point.x)