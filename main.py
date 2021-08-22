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
from chess_pieces import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import QPainter, QPen, QColor, QBrush, QFont
from PIL import Image

#chess_board = [[0 for col in range(11)] for row in range(10)]

im = Image.open('./chess_pieces_img/w_pawn_png_shadow_100px.png')
w_pawn = im.load()
im = Image.open('./chess_pieces_img/w_rook_png_shadow_100px.png')
w_rook = im.load()
im = Image.open('./chess_pieces_img/w_knight_png_shadow_100px.png')
w_knight = im.load()
im = Image.open('./chess_pieces_img/w_queen_png_shadow_100px.png')
w_queen = im.load()
im = Image.open('./chess_pieces_img/w_bishop_png_shadow_100px.png')
w_bishop = im.load()
im = Image.open('./chess_pieces_img/w_king_png_shadow_100px.png')
w_king = im.load()

im = Image.open('./chess_pieces_img/b_pawn_png_shadow_100px.png')
b_pawn = im.load()
im = Image.open('./chess_pieces_img/b_rook_png_shadow_100px.png')
b_rook = im.load()
im = Image.open('./chess_pieces_img/b_knight_png_shadow_100px.png')
b_knight = im.load()
im = Image.open('./chess_pieces_img/b_queen_png_shadow_100px.png')
b_queen = im.load()
im = Image.open('./chess_pieces_img/b_bishop_png_shadow_100px.png')
b_bishop = im.load()
im = Image.open('./chess_pieces_img/b_king_png_shadow_100px.png')
b_king = im.load()

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
        piece_init(white_pieces, black_pieces)

    def chess_piece_print(self, qp, piece_data, value):
        red = 0
        green = 0
        blue = 0
        transparent = 0
        for i in range(100):
            for j in range(100):
                rgb = piece_data[i, j]
                red = rgb[0]
                green = rgb[1]
                blue = rgb[2]
                transparent = rgb[3]
                qp.setPen(QColor(red, green, blue, transparent))
                qp.drawPoint(value.x * 100 + i, value.y * 100 + j)

    def chess_pieces_print(self, qp):
        for key, value in white_pieces.items():
            if value.kinds == 'PAWN':
                self.chess_piece_print(qp, w_pawn, value)
            if value.kinds == 'ROOK':
                self.chess_piece_print(qp, w_rook, value)
            if value.kinds == 'KINGHT':
                self.chess_piece_print(qp, w_knight, value)
            if value.kinds == 'BISHOP':
                self.chess_piece_print(qp, w_bishop, value)
            if value.kinds == 'QUEEN':
                self.chess_piece_print(qp, w_queen, value)
            if value.kinds == 'KING':
                self.chess_piece_print(qp, w_king, value)
        for key, value in black_pieces.items():
            if value.kinds == 'PAWN':
                self.chess_piece_print(qp, b_pawn, value)
            if value.kinds == 'ROOK':
                self.chess_piece_print(qp, b_rook, value)
            if value.kinds == 'KINGHT':
                self.chess_piece_print(qp, b_knight, value)
            if value.kinds == 'BISHOP':
                self.chess_piece_print(qp, b_bishop, value)
            if value.kinds == 'QUEEN':
                self.chess_piece_print(qp, b_queen, value)
            if value.kinds == 'KING':
                self.chess_piece_print(qp, b_king, value)

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
                for name, piece in white_pieces.items():
                    if name == self.name:
                        if name in white_pieces:
                            white_pieces[name].x = int(self.move_select_x)
                            white_pieces[name].y = int(self.move_select_y)
                        for name, piece in list(black_pieces.items()):
                            if piece.x == self.move_select_x and piece.y == self.move_select_y:
                                del black_pieces[name]
            elif self.color == 'black':
                for name, piece in black_pieces.items():
                    if name == self.name:
                        if name in black_pieces:
                            black_pieces[name].x = int(self.move_select_x)
                            black_pieces[name].y = int(self.move_select_y)
                        for name, piece in list(white_pieces.items()):
                            if piece.x == self.move_select_x and piece.y == self.move_select_y:
                                del white_pieces[name]
            self.color = None
            self.update()
            self.move_select_x = -1
            self.move_select_y = -1

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
        self.chess_pieces_print(qp)
#        qp.setFont(QFont('Arial', 26))
#        for key, value in white_pieces.items():
#            qp.setPen(QPen(Qt.red, 3))
#            qp.drawText((value.x) * 100 + 10, (value.y) * 100 + 50, value.kinds)
#        for key, value in black_pieces.items():
#            qp.setPen(QPen(Qt.blue, 3))
#            qp.drawText((value.x) * 100 + 10, (value.y) * 100 + 50, value.kinds)

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

    def piece_can_move(self, e, white_pieces, black_pieces, color_turn, x, y):
        white_turn = 0
        black_turn = 1
        if color_turn == white_turn:
            for key, value in white_pieces.items():
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
            for key, value in black_pieces.items():
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

    def piece_move(self, white_pieces, black_pieces, x, y):
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
        global white_pieces
        global black_pieces
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
                    self.piece_select(white_pieces, black_pieces, white_turn, x, y)
                    if self.color != 'white':
                        white_status == 0
                    else:
                        self.piece_can_move(e, white_pieces, black_pieces, white_turn, x, y)
                        self.update()
                elif white_status == 1:
                    self.piece_move(white_pieces, black_pieces, x, y)
                    white_status = 0
            else:
                if black_status == 0:
                    self.piece_select(white_pieces, black_pieces, black_turn, x, y)
                    if self.color != 'black':
                        black_status == 0
                    else:
                        self.piece_can_move(e, white_pieces, black_pieces, black_turn, x, y)
                        self.update()
                elif black_status == 1:
                    self.piece_move(white_pieces, black_pieces, x, y)
                    black_status = 0
            print("#############################################")
            print('################now turn : {}################'.format(turn))
            print("#############################################")

    def piece_select(self, white_pieces, black_pieces, color_turn, x, y):
        global white_status
        global black_status
        white_turn = 0
        black_turn = 1
        status = 0

        if color_turn == white_turn:
            for key, value in white_pieces.items():
                if value.x == x and value.y == y:
                    self.color = value.color
                    white_status = 1
        else: #elif color_turn == black_turn:
            for key, value in black_pieces.items():
                if value.x == x and value.y == y:
                    self.color = value.color
                    black_status = 1
        if color_turn == white_turn and white_status == 0:
            print("#############################################")
            print("#########please white_pieces choice###########")
            print("#############################################")
        elif color_turn == black_turn and black_status == 0:
            print("#############################################")
            print("#########please black_pieces choice###########")
            print("#############################################")
            
# ================= class end ==================


def main():
    app = QApplication(sys.argv)
    ex = MyApp()
    sys.exit(app.exec_())
    
if __name__  == '__main__':
    main()
