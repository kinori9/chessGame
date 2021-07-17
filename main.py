import sys
import math
import collections
import const
from global_var import *
from get_piece_list import *
from chess_piece import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import QPainter, QPen, QColor, QBrush, QFont

#chess_board = [[0 for col in range(11)] for row in range(10)]

# ================= class start ===================

class MyApp(QWidget):

# ===================== init ======================

    def __init__(self):
        super().__init__()
        self.initUI()
        self.setMouseTracking(False)
        self.select_x = -1
        self.select_y = -1
        self.kinds = None
        self.can_move_list = []
        
    def initUI(self):
        self.setWindowTitle('chess game')
        self.move(100, 100)
        self.resize(800, 800)
        self.show()
        print("piece init start")
        piece_init(white_piece, black_piece)
        print("piece init end")
        #print('white_piece : {},  black_piece : {}', white_piece, black_piece)

# ================ chees_board setting ==================

    def paintEvent(self, e):
        qp = QPainter()
        qp.begin(self)
        self.draw_init_chessBoard(qp)
        self.draw_init_chessPiece(qp)
        print('self.select_x : {} self.select_y {}'.format(self.select_x, self.select_y))
        if self.select_x != -1 and self.select_y != -1:
            self.write_list_can_move()
            self.draw_piece_can_move(qp)
            self.select_x = -1
            self.select_y = -1
        qp.end()
        
    def write_list_can_move(self):
        if self.kinds == 'PAWN':
            self.can_move_list.extend(get_pawn_list(self.select_x, self.select_y, self.kinds))
            print('can move {}'.format(self.kinds))
        elif self.kinds == 'ROOK':
            #self.can_move_list.extend(get_rook_list(self.select_x, self.select_y, self.kinds))
            print('can move {}'.format(self.kinds))
        elif self.kinds == 'KINGHT':
            #self.can_move_list.extend(get_kinght_list(self.select_x, self.select_y, self.kinds))
            print('can move {}'.format(self.kinds))
        elif self.kinds == 'BISHOP':
            #self.can_move_list.extend(get_bishop_list(self.select_x, self.select_y, self.kinds))
            print('can move {}'.format(self.kinds))
        elif self.kinds == 'QUEEN':
            #self.can_move_list.extend(get_queen_list(self.select_x, self.select_y, self.kinds))
            print('can move {}'.format(self.kinds))
        else:
            #self.can_move_list.extend(get_king_list(self.select_x, self.select_y, self.kinds))
            print('can move {}'.format(self.kinds))
        #self.list.append()

    # recive list draw
    def draw_piece_can_move(self, qp):
        qp.setFont(QFont('Arial', 26))
        qp.setPen(QPen(Qt.blue, 3))
        for lst in self.can_move_list:
            print('can_move_list : {}'.format(lst))
        print(self.can_move_list)
        can_move_list = self.can_move_list
        for piece in can_move_list:
            location = str(piece).split(',')
            print(location)
            x = int(location[0])
            y = int(location[1])
            qp.drawText(x, y, 'can move')
        
    def draw_init_chessPiece(self, qp):
        x = 100
        y = 0

        qp.setFont(QFont('Arial', 26))
        qp.setPen(QPen(Qt.gray, 3))
        for key, value in white_piece.items():
           qp.drawText((value.x) * 100 + 10, (value.y) * 100 + 50, value.kinds)
        for key, value in black_piece.items():
           qp.drawText((value.x) * 100 + 10, (value.y) * 100 + 50, value.kinds)

    def draw_init_chessBoard(self, qp):
        qp.setPen(QPen(Qt.black, 1))
        qp.setBrush(QColor(0, 0, 0))
        for x in range(0, 800, 100):
            if (x / 100) % 2 == 1:
                for y in range (100, 800, 200):
                    qp.drawRect(x, y, 100, 100)
            else:
                for y in range (0, 800, 200):
                    qp.drawRect(x, y, 100, 100)
            #print('{}, 0, {}, 100'.format(x, x + 100))
        print("chess_board setting compelete")
        
# ================ mouse setting ==================

    def keyPressEvent(self, e):
        if e.key() == Qt.Key_Escape:
            self.close()
        if e.key() == Qt.Key_F:
            self.showFullScreen()
        if e.key() == Qt.Key_M:
            self.showNormal()

    def piece_can_move(self, e, white_piece, black_piece, color, x, y):
        can_x = -1
        cna_y = -1
        white = 0
        black = 1
        print('--------piece can move---------')
        #print(white_piece)
        if color == white:
            for key, value in white_piece.items():
                if value.x == x and value.y == y:
                    print('x : {}, y : {}'.format(x, y))
                    if value.kinds == 'PAWN':
                        self.select_x = value.x 
                        self.select_y = value.y
                        self.kinds = value.kinds
                        print(key)
                    if value.kinds == 'ROOK':
                        print(key)
                    if value.kinds == 'KINGHT':
                        print(key)
                    if value.kinds == 'BISHOP':
                        print(key)
                    if value.kinds == 'QUEEN':
                        print(key)
                    if value.kinds == 'KING':
                        print(key)
        #if color == white:
        #    print()
        print('--------piece can move---------')

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
            if turn % 2 == white:
                if white_status == 0:
                    piece_select(white_piece, black_piece, white, x, y)
                    self.piece_can_move(e, white_piece, black_piece, white, x, y)
                    self.update()
                else:
                    piece_move(white_piece, black_piece, white)
                    white_status = 0
            else:
                if black_status == 0:
                    piece_select(white_piece, black_piece, black, x, y)
                    self.piece_can_move(e, white_piece, black_piece, black, x, y)
                else:
                    piece_move(white_piece, black_piece, black)
                    black_status = 0
            print('---------------------------')
            print('turn : {}\nwhite_status : {}\nblack_status : {}\n'.format(turn, white_status, black_status))
            print('---------------------------')
            
# ================= class end ==================
    
def piece_move(white_piece, black_piece, color):
    global turn 
    white = 0
    black = 1

    print('---------------------------')
    if color == white:
        print('white')
    else:
        print('black')
    print('piece_move') 
    if color == white:
        turn = black
    else:
        turn = white
    print('---------------------------')

def piece_select(white_piece, black_piece, color, x, y):
    global white_status
    global black_status
    white = 0
    black = 1
    status = 0
    print('---------------------------')
    print('piece_select') 

    if color == white:
        for key, value in white_piece.items():
            if value.x == x and value.y == y:
                print('choice piece : {}'.format(key))
                white_status = 1
        print('white')
    else:
        for key, value in black_piece.items():
            if value.x == x and value.y == y:
                print('choice piece : {}'.format(key))
                black_status = 1
        print('black')
    if color == white and white_status == 0:
        print("please white_piece choice")
    elif color == black and black_status == 0:
        print("please black_piece choice")
    print('---------------------------')

def main():
    app = QApplication(sys.argv)
    ex = MyApp()
    sys.exit(app.exec_())
    
if __name__  == '__main__':
    main()
