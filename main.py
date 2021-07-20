import sys
import math
import collections
import const
from global_var import *
from get_pawn_list import *
from get_rook_list import *
from get_kinght_list import *
from get_bishop_list import *
from get_king_list import *
from location_cal import *
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
        self.name = None
        self.select_x = -1
        self.select_y = -1
        self.move_select_x = -1
        self.move_select_y = -1
        self.kinds = None
        self.can_move_list = []
        self.color = None
        
    def initUI(self):
        self.setWindowTitle('chess game')
        self.move(100, 100)
        self.resize(800, 800)
        self.show()
        piece_init(white_piece, black_piece)

# ================ chees_board setting ==================
    def change_value_select_location(self, qp):
        if self.select_x != -1 and self.select_y != -1:
            self.write_list_can_move()
            self.draw_piece_can_move(qp)
            self.select_x = -1
            self.select_y = -1

    def change_piece_location(self, qp):
        if self.move_select_x != -1 and self.move_select_y != -1:
            if self.color == 'white':
                for name, piece in white_piece.items():
                    if name == self.name:
                        if name in white_piece:
                            white_piece[name].x = int(self.move_select_x)
                            white_piece[name].y = int(self.move_select_y)
                        for name, piece in list(black_piece.items()):
                            if piece.x == self.move_select_x and piece.y == self.move_select_y:
                                del black_piece[name]
            elif self.color == 'black':
                for name, piece in black_piece.items():
                    if name == self.name:
                        if name in black_piece:
                            black_piece[name].x = int(self.move_select_x)
                            black_piece[name].y = int(self.move_select_y)
                        for name, piece in list(white_piece.items()):
                            if piece.x == self.move_select_x and piece.y == self.move_select_y:
                                del white_piece[name]
            self.color = None
            self.update()
            self.move_select_x = -1
            self.move_select_y = -1
            try:
                if white_piece['KING']:
                    pass
            except KeyError:
                print('black win')
                self.close()
            try:
                if black_piece['KING']:
                    pass
            except KeyError:
                print('white win')
                self.close()

    def paintEvent(self, e):
        qp = QPainter()
        qp.begin(self)
        ###### draw Event #####
        self.draw_init_chessBoard(qp)
        self.draw_init_chessPiece(qp)
        self.change_value_select_location(qp)
        self.change_piece_location(qp)
        ######################
        qp.end()
        
    def write_list_can_move(self):
        self.can_move_list.clear()
        if self.kinds == 'PAWN':
            self.can_move_list.extend(get_pawn_list(self.select_x, self.select_y, self.color))
        elif self.kinds == 'ROOK':
            self.can_move_list.extend(get_rook_list(self.select_x, self.select_y, self.color))
        elif self.kinds == 'KINGHT':
            self.can_move_list.extend(get_kinght_list(self.select_x, self.select_y, self.color))
        elif self.kinds == 'BISHOP':
            self.can_move_list.extend(get_bishop_list(self.select_x, self.select_y, self.color))
        elif self.kinds == 'QUEEN':
            print('queen')
            self.can_move_list.extend(get_rook_list(self.select_x, self.select_y, self.color))
            self.can_move_list.extend(get_bishop_list(self.select_x, self.select_y, self.color))
            print('can move {}'.format(self.kinds))
        elif self.kinds == 'KING':
            self.can_move_list.extend(get_king_list(self.select_x, self.select_y, self.color))
            print('can move {}'.format(self.kinds))
        else:
            print('error message')
        #self.list.append()

    # recive list draw
    def draw_piece_can_move(self, qp):
        qp.setFont(QFont('Arial', 26))
        qp.setPen(QPen(Qt.gray, 3))
        can_move_list = self.can_move_list
        for piece in can_move_list:
            location = str(piece).split(',')
            x = int(location[0]) * 100 + 10 
            y = int(location[1]) * 100 + 50
            qp.drawText(x, y, 'can move')
        
    def draw_init_chessPiece(self, qp):
        x = 100
        y = 0

        qp.setFont(QFont('Arial', 26))
        for key, value in white_piece.items():
            qp.setPen(QPen(Qt.red, 3))
            qp.drawText((value.x) * 100 + 10, (value.y) * 100 + 50, value.kinds)
        for key, value in black_piece.items():
            qp.setPen(QPen(Qt.blue, 3))
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
        
# ================ mouse setting ==================

    def keyPressEvent(self, e):
        if e.key() == Qt.Key_Escape:
            self.close()
        if e.key() == Qt.Key_F:
            self.showFullScreen()
        if e.key() == Qt.Key_M:
            self.showNormal()

    def piece_can_move(self, e, white_piece, black_piece, color_turn, x, y):
        white_turn = 0
        black_turn = 1
        if color_turn == white_turn:
            for key, value in white_piece.items():
                if value.x == x and value.y == y:
                    print('x : {}, y : {}'.format(x, y))
                    if value.kinds == 'PAWN':
                        self.name, self.select_x, self.select_y, self.kinds, self.color = key, value.x, value.y, value.kinds, value.color
                    if value.kinds == 'ROOK':
                        self.name, self.select_x, self.select_y, self.kinds, self.color = key, value.x, value.y, value.kinds, value.color
                    if value.kinds == 'KINGHT':
                        self.name, self.select_x, self.select_y, self.kinds, self.color = key, value.x, value.y, value.kinds, value.color
                    if value.kinds == 'BISHOP':
                        self.name, self.select_x, self.select_y, self.kinds, self.color = key, value.x, value.y, value.kinds, value.color
                    if value.kinds == 'QUEEN':
                        self.name, self.select_x, self.select_y, self.kinds, self.color = key, value.x, value.y, value.kinds, value.color
                    if value.kinds == 'KING':
                        self.name, self.select_x, self.select_y, self.kinds, self.color = key, value.x, value.y, value.kinds, value.color
        elif color_turn == black_turn:
            for key, value in black_piece.items():
                if value.x == x and value.y == y:
                    if value.kinds == 'PAWN':
                        self.name, self.select_x, self.select_y, self.kinds, self.color = key, value.x, value.y, value.kinds, value.color
                    if value.kinds == 'ROOK':
                        self.name, self.select_x, self.select_y, self.kinds, self.color = key, value.x, value.y, value.kinds, value.color
                    if value.kinds == 'KINGHT':
                        self.name, self.select_x, self.select_y, self.kinds, self.color = key, value.x, value.y, value.kinds, value.color
                    if value.kinds == 'BISHOP':
                        self.name, self.select_x, self.select_y, self.kinds, self.color = key, value.x, value.y, value.kinds, value.color
                    if value.kinds == 'QUEEN':
                        self.name, self.select_x, self.select_y, self.kinds, self.color = key, value.x, value.y, value.kinds, value.color
                    if value.kinds == 'KING':
                        self.name, self.select_x, self.select_y, self.kinds, self.color = key, value.x, value.y, value.kinds, value.color

    def piece_move(self, white_piece, black_piece, x, y):
        global turn
        check = False
        fix_x = 10
        fix_y = 50
        for can_move in self.can_move_list:
            tmp_x = int(can_move.split(',')[0])
            tmp_y = int(can_move.split(',')[1])
            if x == tmp_x and y == tmp_y:
                self.move_select_x = x
                self.move_select_y = y
                check = True
        if check == True:
            turn += 1
        self.update()
        self.can_move_list.clear()
            
    def mousePressEvent(self, e):
        global turn
        global white_piece
        global black_piece
        global white_status
        global black_status
        white_turn = 0
        black_turn = 1

        if e.buttons() & Qt.LeftButton:
            x = math.trunc(e.x() / 100)
            y = math.trunc(e.y() / 100)
            print('x : {} y: {}'.format(x, y))
            if turn % 2 == white_turn:
                if white_status == 0:
                    self.piece_select(white_piece, black_piece, white_turn, x, y)
                    if self.color != 'white':
                        white_status == 0
                    else:
                        self.piece_can_move(e, white_piece, black_piece, white_turn, x, y)
                        self.update()
                elif white_status == 1:
                    self.piece_move(white_piece, black_piece, x, y)
                    white_status = 0
            else:
                if black_status == 0:
                    self.piece_select(white_piece, black_piece, black_turn, x, y)
                    if self.color != 'black':
                        black_status == 0
                    else:
                        self.piece_can_move(e, white_piece, black_piece, black_turn, x, y)
                        self.update()
                elif black_status == 1:
                    self.piece_move(white_piece, black_piece, x, y)
                    black_status = 0
            print("#############################################")
            print('################now turn : {}################'.format(turn))
            print("#############################################")

    def piece_select(self, white_piece, black_piece, color_turn, x, y):
        global white_status
        global black_status
        white_turn = 0
        black_turn = 1
        status = 0

        if color_turn == white_turn:
            for key, value in white_piece.items():
                if value.x == x and value.y == y:
                    self.color = value.color
                    white_status = 1
        else: #elif color_turn == black_turn:
            for key, value in black_piece.items():
                if value.x == x and value.y == y:
                    self.color = value.color
                    black_status = 1
        if color_turn == white_turn and white_status == 0:
            print("#############################################")
            print("#########please white_piece choice###########")
            print("#############################################")
        elif color_turn == black_turn and black_status == 0:
            print("#############################################")
            print("#########please black_piece choice###########")
            print("#############################################")
            
# ================= class end ==================


def main():
    app = QApplication(sys.argv)
    ex = MyApp()
    sys.exit(app.exec_())
    
if __name__  == '__main__':
    main()
