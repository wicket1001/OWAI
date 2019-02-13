import sys

from PyQt5.QtCore import pyqtSignal, QBasicTimer, Qt, QSize
from PyQt5.QtGui import QPainter
from PyQt5.QtWidgets import QFrame

from v1_0.Entity import *


class Board(QFrame):
    msg2Status_bar = pyqtSignal(str)

    BoardWidth = 25
    BoardHeight = 25
    Speed = 300

    def __init__(self, parent, network, size):
        super().__init__(parent)
        self.network = network
        self.size = size

        self.timer = QBasicTimer()
        self.entities = []

        self.isWaitingAfterLine = False

        self.numLinesRemoved = 0
        self.board = []

        self.setFocusPolicy(Qt.StrongFocus)
        self.isStarted = False
        self.isPaused = False
        self.clear_board()

    def __str__(self):
        out = ""
        for i in range(Board.BoardHeight):
            for j in range(Board.BoardWidth):
                out += str(self.field_at(i, j)) + ", "
            out += "\n"
        return out

    def sizeHint(self):
        return QSize(self.size.height(), self.size.width() // 2)

    def minimumSizeHint(self):
        return QSize(400, 200)

    def initialise_board(self):
        self.clear_board()
        for i in range(Board.BoardHeight):
            for j in range(Board.BoardWidth):
                self.set_field_at(j, Board.BoardHeight - i - 1, random.randint(1, 6))
        for i in range(Board.BoardHeight):
            self.set_field_at(0, Board.BoardHeight - i - 1, Fields.Ocean)
            self.set_field_at(Board.BoardWidth - 1, Board.BoardHeight - i - 1, Fields.Ocean)
        for j in range(Board.BoardWidth):
            self.set_field_at(j, 0, Fields.Ocean)
            self.set_field_at(j, Board.BoardHeight - 1, Fields.Ocean)

    def field_at(self, x, y):
        """determines shape at the board position"""

        return self.board[(y * Board.BoardWidth) + x]

    def set_field_at(self, x, y, field):
        """sets a shape at the board"""

        self.board[(y * Board.BoardWidth) + x] = field

    def square_width(self):
        """returns the width of one square"""

        return (min(self.contentsRect().height(), self.contentsRect().width()) //
                min(Board.BoardHeight, Board.BoardWidth))

    def square_height(self):
        """returns the height of one square"""

        return (min(self.contentsRect().height(), self.contentsRect().width()) //
                min(Board.BoardHeight, Board.BoardWidth))

    def start(self):
        """starts game"""

        if self.isPaused:
            return

        self.isStarted = True
        self.isWaitingAfterLine = False
        self.numLinesRemoved = 0
        self.clear_board()
        self.initialise_board()

        self.msg2Status_bar.emit(str(self.numLinesRemoved))

        self.spawn_initial(100)
        self.timer.start(Board.Speed, self)

    def pause(self):
        """pauses game"""

        if not self.isStarted:
            return

        self.isPaused = not self.isPaused

        if self.isPaused:
            self.timer.stop()
            self.msg2Status_bar.emit("paused")

        else:
            self.timer.start(Board.Speed, self)
            self.msg2Status_bar.emit(str(self.numLinesRemoved))

        self.update()

    def paintEvent(self, event):
        print("Every time to paint")
        """paints all shapes of the game"""

        painter = QPainter(self)
        rect = self.contentsRect()

        board_top = rect.bottom() - Board.BoardHeight * self.square_height()

        '''
        for i in range(Board.BoardHeight):
            for j in range(Board.BoardWidth):
                shape = self.shapeAt(j, Board.BoardHeight - i - 1)

                if shape != Tetrominoe.NoShape:
                    self.drawSquare(painter,
                                    rect.left() + j * self.squareWidth(),
                                    board_top + i * self.squareHeight(), shape)

        if self.curPiece.shape() != Tetrominoe.NoShape:

            for i in range(4):
                x = self.curX + self.curPiece.x(i)
                y = self.curY - self.curPiece.y(i)
                self.drawSquare(painter, rect.left() + x * self.squareWidth(),
                                board_top + (Board.BoardHeight - y - 1) * self.squareHeight(),
                                self.curPiece.shape())
        '''
        for i in range(Board.BoardHeight):
            for j in range(Board.BoardWidth):
                field = self.field_at(j, Board.BoardHeight - i - 1)


                color = Fields.color_table[field]

                Drawer.draw_square(painter,
                                   rect.left() + j * self.square_width(),
                                   board_top + i * self.square_height(),
                                   (self.square_height(), self.square_width()),
                                   color)
        for i in range(len(self.entities)):
            self.entities[i].draw(painter, (self.square_height() // 2, self.square_width() // 2))
        self.network.draw(painter)

        for i in range(len(Fields.color_table)):
            print(i, hex(Fields.color_table[i]).upper())

    def keyPressEvent(self, event):
        """processes key press events"""

        if not self.isStarted:  # or self.curPiece.shape() == Fields.NoField:
            super(Board, self).keyPressEvent(event)
            return

        key = event.key()

        if key == Qt.Key_Escape:
            self.close()
            sys.exit(0)

        if key == Qt.Key_P:
            self.pause()
            return

        if self.isPaused:
            return

        '''
        elif key == Qt.Key_Left:
            self.try_move(self.curPiece, self.curX - 1, self.curY)

        elif key == Qt.Key_Right:
            self.try_move(self.curPiece, self.curX + 1, self.curY)

        elif key == Qt.Key_Down:
            self.try_move(self.curPiece.rotateRight(), self.curX, self.curY)

        elif key == Qt.Key_Up:
            self.try_move(self.curPiece.rotateLeft(), self.curX, self.curY)

        elif key == Qt.Key_Space:
            self.dropDown()

        elif key == Qt.Key_D:
            self.oneLineDown()
        '''

        super(Board, self).keyPressEvent(event)

    def timerEvent(self, event):
        """handles timer event"""

        if event.timerId() == self.timer.timerId():

            if self.isWaitingAfterLine:
                self.isWaitingAfterLine = False
                self.spawn_entities()
            else:
                pass
                # self.oneLineDown()

        else:
            super(Board, self).timerEvent(event)

    def clear_board(self):
        """clears shapes from the board"""

        self.board = []
        for i in range(Board.BoardHeight * Board.BoardWidth):
            self.board.append(Fields.NoField)
        self.entities = []

    '''
    def dropDown(self):
        """drops down a shape"""

        newY = self.curY

        while newY > 0:

            if not self.tryMove(self.curPiece, self.curX, newY - 1):
                break

            newY -= 1

        self.pieceDropped()

    def oneLineDown(self):
        """goes one line down with a shape"""

        if not self.tryMove(self.curPiece, self.curX, self.curY - 1):
            self.pieceDropped()
    '''

    '''
    def pieceDropped(self):
        """after dropping shape, remove full lines and create new shape"""

        for i in range(4):
            x = self.curX + self.curPiece.x(i)
            y = self.curY - self.curPiece.y(i)
            self.setShapeAt(x, y, self.curPiece.shape())

        self.removeFullLines()

        if not self.isWaitingAfterLine:
            self.spawnEntities()

    def removeFullLines(self):
        """removes all full lines from the board"""

        numFullLines = 0
        rowsToRemove = []

        for i in range(Board.BoardHeight):

            n = 0
            for j in range(Board.BoardWidth):
                if not self.fieldAt(j, i) == Fields.NoField:
                    n = n + 1

            if n == 10:
                rowsToRemove.append(i)

        rowsToRemove.reverse()

        for m in rowsToRemove:

            for k in range(m, Board.BoardHeight):
                for l in range(Board.BoardWidth):
                    self.setShapeAt(l, k, self.fieldAt(l, k + 1))

        numFullLines = numFullLines + len(rowsToRemove)

        if numFullLines > 0:
            self.numLinesRemoved = self.numLinesRemoved + numFullLines
            self.msg2Statusbar.emit(str(self.numLinesRemoved))

            self.isWaitingAfterLine = True
            self.curPiece.initialise(Fields.NoField)
            self.update()
    '''

    def spawn_initial(self, n=100):
        for x in range(n):
            self.spawn_entities()

    def spawn_entities(self):
        """creates a new shape"""

        self.entities.append(Entity((self.square_height(), self.square_width())))
        '''
        self.curPiece = Entity()
        self.curPiece.spawnRandomEntity()
        self.curX = Board.BoardWidth // 2 + 1
        self.curY = Board.BoardHeight - 1 + self.curPiece.minY()

        if not self.tryMove(self.curPiece, self.curX, self.curY):
            self.curPiece.initialise(Fields.NoField)
            self.timer.stop()
            self.isStarted = False
            self.msg2Statusbar.emit("Game over")
        '''

    '''
    def try_move(self, newPiece, newX, newY):
        """tries to move a shape"""

        for i in range(4):

            x = newX + newPiece.x(i)
            y = newY - newPiece.y(i)

            if x < 0 or x >= Board.BoardWidth or y < 0 or y >= Board.BoardHeight:
                return False

            if self.fieldAt(x, y) != Fields.NoField:
                return False

        self.curPiece = newPiece
        self.curX = newX
        self.curY = newY
        self.update()

        return True
    '''


class Fields(object):
    NoField = 0
    Grass = 1
    Wood = 2
    Stone = 3
    Wheat = 4
    Water = 5
    Ocean = 6
    Dead = 7

    color_table = [0x000000, 0x66DD66, 0x229922, 0xCCCCCC, 0xCCCC66, 0x66CCCC, 0x3333DD, 0x444444]