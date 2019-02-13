from PyQt5.QtWidgets import QMainWindow, QDesktopWidget, QApplication, QDockWidget

from v1_0.Network import *


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


if __name__ == '__main__':
    app = QApplication([])
    owai = OWAI()
    sys.exit(app.exec_())
