"""
Decouples an abstraction from its implementation

Notes from (https://bit.ly/2xzayOd):

Useful when code often changes in implementation and usage.

Client Object <=> Provider Object

Each client can interact with each provider of an operation
in a system. However, if the implementation of the provider/client
changes either/or client/provider will have to change. The solution is
to add a bridge which the clients will actually call that contains a 
reference to providers

Client <=> Bridge <=> Provider
"""

class DrawingAPI1:
    """Provider class 1"""
    def draw_circle(self, x, y, radius):
        print("API 1 for drawing a circle at {}:{} radius {}".format(x, y, radius))


class DrawingAPI2:
    """Provider class 2"""
    def draw_circle(self, x, y, radius):
        print("API 2 for drawing a circle at {}:{} radius {}".format(x, y, radius))


class CircleShape:
    """Abstraction"""
    def __init__(self, x, y, radius, drawing_api):
        self._x = x
        self._y = y
        self._radius = radius
        self._drawing_api = drawing_api

    
    def draw(self):
        """Low level implementation specific method, specified at instanstiation"""
        self._drawing_api.draw_circle(self._x, self._y, self._radius)

    def scale(self, pct):
        """High level abstraction specific method"""
        self._radius *=pct

def main():
    shape = CircleShape(0, 0, 5, DrawingAPI1())
    shape.draw()
    shape.scale(2.5)
    shape.draw()

if __name__ == "__main__":
    main()
