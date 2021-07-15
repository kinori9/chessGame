import sys
import math
import collections
import const
from chess_piece import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import QPainter, QPen, QColor, QBrush, QFont

#chess_board = [[0 for col in range(11)] for row in range(10)]
turn = 0
map_x = 7
map_y = 7
white_status = 0
black_status = 0
white_piece = {}
black_piece = {}

# ================= class start ===================

class MyApp(QWidget):

# ===================== init ======================

    def __init__(self):
        super().__init__()
        self.initUI()
        self.setMouseTracking(True)
        
    def initUI(self):
        #self.statusBar().showMessage('Ready')
        self.setWindowTitle('chess game')
        self.move(100, 100)
        self.resize(800, 800)
        self.show()
        print("piece init start")
        piece_init(white_piece, black_piece)
        print("piece init end")

# ================ chees_board setting ==================

    def paintEvent(self, e):
        qp = QPainter()
        qp.begin(self)
        self.draw_init_chessBoard(qp)
        self.draw_init_chessPiece(qp)
        qp.end()

    def draw_init_chessPiece(self, qp):
        x = 100
        y = 0
        global white_piece
        global black_piece

        qp.setFont(QFont('Arial', 26))
        qp.setPen(QPen(Qt.gray, 3))
        for key, value in white_piece.items():
           qp.drawText((value.x) * 100 + 10, (value.y) * 100 + 50, value.name)
        for key, value in black_piece.items():
           qp.drawText((value.x) * 100 + 10, (value.y) * 100 + 50, value.name)

    def draw_init_chessBoard(self, qp):
        qp.setPen(QPen(Qt.black, 1))
        qp.setBrush(QColor(0, 0, 0))
        for x in range(0, 800, 100):
            if ((x / 100) % 2 == 1):
                for y in range (100, 800, 200):
                    qp.drawRect(x, y, 100, 100)
            else:
                for y in range (0, 800, 200):
                    qp.drawRect(x, y, 100, 100)
            print('{}, 0, {}, 100'.format(x, x + 100))
        print("chess_board setting compelete")
        
# ================ mouse setting ==================

    def keyPressEvent(self, e):
        if e.key() == Qt.Key_Escape:
            self.close()
        if e.key() == Qt.Key_F:
            self.showFullScreen()
        if e.key() == Qt.Key_M:
            self.showNormal()

    def mousePressEvent(self, e):
        global turn
        global white_piece
        global black_piece
        global white_status
        global black_status
        white = 0
        black = 1

        if e.buttons() & Qt.LeftButton:
            x = math.trunc(e.x() / 100)
            y = math.trunc(e.y() / 100)
            print('x : {} y: {}'.format(x, y))
            if (turn % 2 == white):
                if (white_status == 0):
                    piece_select(white_piece, black_piece, white, x, y)
                    piece_can_move(white_piece, black_piece, white, x, y)
                    white_status = 1
                elif (white_status == 1):
                    piece_move(white_piece, black_piece, white)
                    piece_can_move(white_piece, black_piece, white, x, y)
                    white_status = 0
            else:
                if (black_status == 0):
                    piece_select(white_piece, black_piece, black, x, y)
                    black_status = 1
                elif (black_status == 1):
                    piece_move(white_piece, black_piece, black)
                    black_status = 0
            print('turn : {}, white_status : {}, black_status : {}'.format(turn, white_status, black_status))

# ================= class end ==================
    
def piece_move(white_piece, black_piece, kinds):
    global turn 
    white = 0
    black = 1
    if (kinds == white):
        print('white')
    else:
        print('black')
    print('piece_move') 
    if (kinds == white):
        turn = black
    else:
        turn = white
######start######
def piece_select(white_piece, black_piece, kinds, x, y):
    white = 0
    black = 1
    if (kinds == white):
        for key, value in white_piece.items():
            if (value.x == x and value.y == y):
                print('choice piece : {}'.format(key))
        print('white')
    else:
        for key, value in black_piece.items():
            if (value.x == x and value.y == y):
                print('choice piece : {}'.format(key))
        print('black')
    print('piece_select') 
    if (kinds == white):
        turn = black
    else:
        turn = white

def main():
    app = QApplication(sys.argv)
    ex = MyApp()
    sys.exit(app.exec_())
    
if __name__ == '__main__':
    main()
