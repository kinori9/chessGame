import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import Qt
import collections
from chess_piece import *

#chess_board = [[0 for col in range(11)] for row in range(10)]

class MyApp(QMainWindow):

# ===================== init ======================
    def __init__(self):
        super().__init__()
        self.initUI()
        self.setWindowTitle('chess game')

        self.setMouseTracking(True)

    def initUI(self):
        self.setWindowTitle('My First Application')
        self.move(100, 100)
        self.resize(800, 800)
        self.statusbar = self.statusbar()
        self.show()

# ================= mouse setting ==================
    def mouseMoveEvent(self, event):
        print(event.x())
        print(event.y())

    def mouseclickEvent(self, buttons):
        if buttons & Qt.LeftButton:
            print('LEFT')
        if buttons & Qt.MidButton:
            print('MIDDLE')
        if buttons & Qt.RightButton:
            print('RIGHT')

    def mousePressEvent(self, e):
        self.mouseButtonKind(e.buttons())

#def white_move(white_piece, black_piece):
    #mouseMoveEvent
#def black_move(white_piece, black_piece):
"""    
def game_start(white_piece, black_piece):
    black = 0
    white = 1
    turn = 1
    while (True):
        if (turn % 2 == black):
            black_move(white_piece, black_piece)
        else:
            white_move(white_piece, black_piece)
        turn += 1
"""

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyApp()

    white_piece = {}
    black_piece = {}
    piece_init(white_piece, black_piece)

    print("chess game start")
    #game_start(white_piece, black_piece) 
    print("chess game end")

    sys.exit(app.exec_())
