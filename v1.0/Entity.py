import random

from Main import Drawer


class Entity(object):
    def __init__(self, size):
        self.x = random.randint(0, 1000)
        self.y = random.randint(0, 1000)
        self.size = size

    def x(self):
        return self.x

    def y(self):
        return self.y

    def draw(self, painter, size):
        # print(self.x, self.y)
        #Drawer.draw_line(painter, (self.x, self.y), (self.x + 10, self.y - 10), (0, 0, 0))
        Drawer.draw_circle(painter,
                           self.x,
                           self.y,
                           size,
                           (255, 0, 0))
        Drawer.draw_line(painter, (self.x, self.y), (max(self.x - 20, 0), max(self.y - 20, 0)), (0, 0, 0))

    '''
    def x(self, index):
        """returns x coordinate"""

        return self.coords[index][0]

    def y(self, index):
        """returns y coordinate"""

        return self.coords[index][1]

    def setX(self, index, x):
        """sets x coordinate"""

        self.coords[index][0] = x

    def setY(self, index, y):
        """sets y coordinate"""

        self.coords[index][1] = y

    def minX(self):
        """returns min x value"""

        m = self.coords[0][0]
        for i in range(4):
            m = min(m, self.coords[i][0])

        return m
        
    def maxX(self):
        """returns max x value"""

        m = self.coords[0][0]
        for i in range(4):
            m = max(m, self.coords[i][0])

        return m

    def minY(self):
        """returns min y value"""

        m = self.coords[0][1]
        for i in range(4):
            m = min(m, self.coords[i][1])

        return m

    def maxY(self):
        """returns max y value"""

        m = self.coords[0][1]
        for i in range(4):
            m = max(m, self.coords[i][1])

        return m

    def rotateLeft(self):
        """rotates shape to the left"""

        if self.pieceShape == Tetrominoe.SquareShape:
            return self

        result = Enitity()
        result.pieceShape = self.pieceShape

        for i in range(4):
            result.setX(i, self.y(i))
            result.setY(i, -self.x(i))

        return result

    def rotateRight(self):
        """rotates shape to the right"""

        if self.pieceShape == Tetrominoe.SquareShape:
            return self

        result = Enitity()
        result.pieceShape = self.pieceShape

        for i in range(4):
            result.setX(i, -self.y(i))
            result.setY(i, self.x(i))

        return result
    '''