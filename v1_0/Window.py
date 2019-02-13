from PyQt5.QtCore import QSize
from PyQt5.QtWidgets import QFrame


class Window(QFrame):
    def __init__(self, parent, offset, size):
        super().__init__(parent)
        self.offset = offset
        self.size = size

    def sizeHint(self):
        return QSize(self.size.height(), self.size.width() // 2)

    def minimumSizeHint(self):
        return QSize(400, 200)

    def sizeHint(self):
        return QSize(self.size.height(), self.size.width() // 3)

    def minimumSizeHint(self):
        return QSize(400, 200)

    def contentsMargins(self):
        return 0

    #@staticmethod
    #def offset():
    #    return 2000, 0  # make dynamic

