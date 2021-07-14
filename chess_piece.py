def piece_init(white_piece, black_piece):
    white_piece['PAWN1'] = Chess_Piece('PAWN', 0, 6, True, 'white')
    white_piece['PAWN2'] = Chess_Piece('PAWN', 1, 6, True, 'white')
    white_piece['PAWN3'] = Chess_Piece('PAWN', 2, 6, True, 'white')
    white_piece['PAWN4'] = Chess_Piece('PAWN', 3, 6, True, 'white')
    white_piece['PAWN5'] = Chess_Piece('PAWN', 4, 6, True, 'white')
    white_piece['PAWN6'] = Chess_Piece('PAWN', 5, 6, True, 'white')
    white_piece['PAWN7'] = Chess_Piece('PAWN', 6, 6, True, 'white')
    white_piece['PAWN8'] = Chess_Piece('PAWN', 7, 6, True, 'white')
    white_piece['ROOK1'] = Chess_Piece('ROOK', 0, 7, True, 'white')
    white_piece['ROOK2'] = Chess_Piece('ROOK', 7, 7, True, 'white')
    white_piece['KNIGHT1'] = Chess_Piece('KINGHT', 1, 7, True, 'white')
    white_piece['KNIGHT2'] = Chess_Piece('KINGHT', 6, 7, True, 'white')
    white_piece['BISHOP1'] = Chess_Piece('BISHOP', 2, 7 ,True, 'white')
    white_piece['BISHOP2'] = Chess_Piece('BISHOP', 5, 7 ,True, 'white')
    white_piece['QUEEN'] = Chess_Piece('QUEEN', 3, 7, True, 'white')
    white_piece['KING'] = Chess_Piece('KING', 4, 7, True, 'white')

    black_piece['PAWN1'] = Chess_Piece('PAWN', 0, 1, True, 'black')
    black_piece['PAWN2'] = Chess_Piece('PAWN', 1, 1, True, 'black')
    black_piece['PAWN3'] = Chess_Piece('PAWN', 2, 1, True, 'black')
    black_piece['PAWN4'] = Chess_Piece('PAWN', 3, 1, True, 'black')
    black_piece['PAWN5'] = Chess_Piece('PAWN', 4, 1, True, 'black')
    black_piece['PAWN6'] = Chess_Piece('PAWN', 5, 1, True, 'black')
    black_piece['PAWN7'] = Chess_Piece('PAWN', 6, 1, True, 'black')
    black_piece['PAWN8'] = Chess_Piece('PAWN', 7, 1, True, 'black')
    black_piece['ROOK1'] = Chess_Piece('ROOK', 0, 0, True, 'black')
    black_piece['ROOK2'] = Chess_Piece('ROOK', 7, 0, True, 'black')
    black_piece['KNIGHT1'] = Chess_Piece('KINGHT', 1, 0, True, 'black')
    black_piece['KNIGHT2'] = Chess_Piece('KINGHT', 6, 0, True, 'black')
    black_piece['BISHOP1'] = Chess_Piece('BISHOP', 2, 0, True, 'black')
    black_piece['BISHOP2'] = Chess_Piece('BISHOP', 5, 0, True, 'black')
    black_piece['QUEEN'] = Chess_Piece('QUEEN', 3, 0, True, 'black')
    black_piece['KING'] = Chess_Piece('KING', 4, 0, True, 'black')

class Chess_Piece:

    def __init__(self, name, x, y, status, kinds):
        self.name = name
        self.x = x
        self.y = y
        self.status = status
        self.kinds = kinds

    def print_name(self):
        print(self.name) 

    def print_x(self):
        print(self.x) 

    def print_y(self):
        print(self.y) 

    def print_status(self):
        print(self.status)

    def print_kinds(self):
        print(self.kinds)

    def print_all(self):
        print(self.name) 
        print(self.x) 
        print(self.y) 
        print(self.status)
        print(self.kinds)
