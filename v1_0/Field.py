from PyQt5.QtGui import QColor


class Field:
    qp = None

    def __init__(self):
        pass

    def setQPainter(self, qp):
        self.qp = qp

    def drawBackground(self):
        self.draw_rectangle((10, 10), (100, 100), (0, 0, 0))

    def draw_rectangle(self, coordinates, size, color):
        self.qp.setBrush(QColor(color[0], color[1], color[2]))
        self.qp.drawRect(coordinates[0], coordinates[1], size[0], size[1])

        '''
        def draw_rectangles(self, qp):
            col = QColor(0, 0, 0)
            col.setNamedColor('#d4d4d4')
            qp.setPen(col)

            qp.setBrush(QColor(200, 0, 0))
            qp.drawRect(10, 15, 90, 60)

            qp.setBrush(QColor(255, 80, 0, 160))
            qp.drawRect(130, 15, 90, 60)

            qp.setBrush(QColor(25, 0, 90, 200))
            qp.drawRect(250, 15, 90, 60)
            '''




