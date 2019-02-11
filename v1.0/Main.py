import sys

from PyQt5.QtCore import Qt, QPoint
from PyQt5.QtGui import QColor
from PyQt5.QtWidgets import QMainWindow, QDesktopWidget, QApplication, QDockWidget

from Board import Board
from Network import Network


class OWAI(QMainWindow):
    def __init__(self):
        super().__init__()

        # self.layout = QtWidgets.QBoxLayout(2)

        self.showFullScreen()

        self.network = Network(self, self.contentsRect())

        self.t_board = Board(self, self.network, self.contentsRect())
        self.setCentralWidget(self.t_board)

        self.items = QDockWidget("Dockable", self)
        self.items.setWidget(self.network)
        self.addDockWidget(Qt.RightDockWidgetArea, self.items)

        # self.t_board.resize(self.contentsRect().height(), self.contentsRect().width() * 0.1)
        # self.items.resize(self.contentsRect().height(), self.contentsRect().width() * 0.2)

        self.status_bar = self.statusBar()
        self.t_board.msg2Status_bar[str].connect(self.status_bar.showMessage)

        self.t_board.start()

        #  self.resize(1000, 1000)
        self.center()
        self.setWindowTitle('Tetris')
        self.show()

    def center(self):
        """centers the window on the screen"""

        screen = QDesktopWidget().screenGeometry()
        size = self.geometry()
        self.move((screen.width() - size.width()) / 2,
                  (screen.height() - size.height()) / 2)


class Drawer:
    @staticmethod
    def draw_circle(painter, x, y, size, color):
        color = QColor(color[0], color[1], color[2])
        center = QPoint(x, y)
        painter.setBrush(color)
        painter.drawEllipse(center, size[0] / 2, size[1] / 2)

    @staticmethod
    def draw_square(painter, x, y, size, color):
        """draws a square of a shape"""
        color = QColor(color)
        painter.fillRect(x + 1, y + 1, size[1] - 2,
                         size[0] - 2, color)

        painter.setPen(color.lighter())
        painter.drawLine(x, y + size[0] - 1, x, y)
        painter.drawLine(x, y, x + size[1] - 1, y)

        painter.setPen(color.darker())
        painter.drawLine(x + 1, y + size[0] - 1,
                         x + size[1] - 1, y + size[0] - 1)
        painter.drawLine(x + size[1] - 1,
                         y + size[0] - 1, x + size[1] - 1, y + 1)

    @staticmethod
    def draw_line(painter, start, end, color):
        # print(start, end)
        color = QColor(color[0], color[1], color[2])
        painter.setPen(color)
        painter.drawLine(start[0], start[0], end[1], end[1])


if __name__ == '__main__':
    app = QApplication([])
    owai = OWAI()
    sys.exit(app.exec_())
