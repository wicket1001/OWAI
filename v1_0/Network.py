import math

from v1_0.Board import *
from v1_0.Drawer import Drawer


class Network(QFrame):
    def __init__(self, parent, size):
        super().__init__(parent)
        self.size = size
        self.layers = (4, 3, 7)
        self.max_nodes = max(self.layers)
        self.nodes = [[]]

    def sizeHint(self):
        return QSize(self.size.height(), self.size.width() // 3)

    def minimumSizeHint(self):
        return QSize(400, 200)

    def contentsMargins(self):
        return 0

    def square_width(self):
        """returns the width of one square"""

        return (min(self.contentsRect().height(), self.contentsRect().width()) //
                min(len(self.layers), self.max_nodes))

    @staticmethod
    def offset():
        return 2000, 0  # make dynamic

    def square_height(self):
        """returns the height of one square"""

        return (min(self.contentsRect().height(), self.contentsRect().width()) //
                min(len(self.layers), self.max_nodes))

    def node_at(self, x, y):
        """determines shape at the board position"""

        #return self.nodes[(y * Board.BoardWidth) + x]
        return self.nodes[x][y]

    def set_node_at(self, x, y, value):
        """sets a shape at the board"""

        # self.board[(y * Board.BoardWidth) + x] = shape
        self.nodes[x][y] = value

    def draw(self, painter):
        print("IT LIVES", self.offset())
        stepX = self.contentsRect().width() // len(self.layers)
        stepY = self.contentsRect().height() // self.max_nodes
        offsetX = self.offset()[0] + stepX / 2
        offsetY = 10 + stepY / 2
        for i in range(len(self.layers)):
            for j in range(self.layers[i]):
                Drawer.draw_circle(painter, offsetX + stepX * i, offsetY + stepY * j,
                                   (self.square_height(), self.square_width()), (0, 0, 0))
            offsetX += stepX

    def clear_network(self):
        """clears shapes from the board"""

        self.nodes = []
        for i in range(len(self.layers)):
            self.nodes.append([])
            for j in range(self.layers[i]):
                self.nodes[i].append(0)

    def initialise_network(self):
        self.clear_network()
        for i in range(len(self.layers)):
            for j in range(self.layers[i]):
                self.set_node_at(j, Board.Board.BoardHeight - i - 1, random.randint(1, 6))

    @staticmethod
    def sigmoid(x):
        return 1 / (1 + math.exp(-x))