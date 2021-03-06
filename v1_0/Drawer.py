from PyQt5.QtCore import QPoint
from PyQt5.QtGui import QColor


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

