def piece_init(white_pieces, black_pieces):
    white_pieces['PAWN1'] = Chess_Piece('PAWN', 0, 6, True, 'white')
    white_pieces['PAWN2'] = Chess_Piece('PAWN', 1, 6, True, 'white')
    white_pieces['PAWN3'] = Chess_Piece('PAWN', 2, 6, True, 'white')
    white_pieces['PAWN4'] = Chess_Piece('PAWN', 3, 6, True, 'white')
    white_pieces['PAWN5'] = Chess_Piece('PAWN', 4, 6, True, 'white')
    white_pieces['PAWN6'] = Chess_Piece('PAWN', 5, 6, True, 'white')
    white_pieces['PAWN7'] = Chess_Piece('PAWN', 6, 6, True, 'white')
    white_pieces['PAWN8'] = Chess_Piece('PAWN', 7, 6, True, 'white')
    white_pieces['ROOK1'] = Chess_Piece('ROOK', 0, 7, True, 'white')
    white_pieces['ROOK2'] = Chess_Piece('ROOK', 7, 7, True, 'white')
    white_pieces['KNIGHT1'] = Chess_Piece('KINGHT', 1, 7, True, 'white')
    white_pieces['KNIGHT2'] = Chess_Piece('KINGHT', 6, 7, True, 'white')
    white_pieces['BISHOP1'] = Chess_Piece('BISHOP', 2, 7 ,True, 'white')
    white_pieces['BISHOP2'] = Chess_Piece('BISHOP', 5, 7 ,True, 'white')
    white_pieces['QUEEN'] = Chess_Piece('QUEEN', 3, 7, True, 'white')
    white_pieces['KING'] = Chess_Piece("KING", 4, 7, True, "white")

    black_pieces['PAWN1'] = Chess_Piece('PAWN', 0, 1, True, 'black')
    black_pieces['PAWN2'] = Chess_Piece('PAWN', 1, 1, True, 'black')
    black_pieces['PAWN3'] = Chess_Piece('PAWN', 2, 1, True, 'black')
    black_pieces['PAWN4'] = Chess_Piece('PAWN', 3, 1, True, 'black')
    black_pieces['PAWN5'] = Chess_Piece('PAWN', 4, 1, True, 'black')
    black_pieces['PAWN6'] = Chess_Piece('PAWN', 5, 1, True, 'black')
    black_pieces['PAWN7'] = Chess_Piece('PAWN', 6, 1, True, 'black')
    black_pieces['PAWN8'] = Chess_Piece('PAWN', 7, 1, True, 'black')
    black_pieces['ROOK1'] = Chess_Piece('ROOK', 0, 0, True, 'black')
    black_pieces['ROOK2'] = Chess_Piece('ROOK', 7, 0, True, 'black')
    black_pieces['KNIGHT1'] = Chess_Piece('KINGHT', 1, 0, True, 'black')
    black_pieces['KNIGHT2'] = Chess_Piece('KINGHT', 6, 0, True, 'black')
    black_pieces['BISHOP1'] = Chess_Piece('BISHOP', 2, 0, True, 'black')
    black_pieces['BISHOP2'] = Chess_Piece('BISHOP', 5, 0, True, 'black')
    black_pieces['QUEEN'] = Chess_Piece('QUEEN', 3, 0, True, 'black')
    black_pieces['KING'] = Chess_Piece('KING', 4, 0, True, 'black')

class Chess_Piece:

    def __init__(self, kinds, x, y, status, color):
        self.kinds = kinds
        self.x = x
        self.y = y
        self.status = status
        self.color = color

    def kinds(self):
        return (self.kinds) 

    def x(self):
        return (self.x) 

    def y(self):
        return (self.y) 

    #def status(self):
        #return (self.status)

    def color(self):
        return (self.color)

    def list_all(self):
        list = []
        list.append(self.kinds)
        list.append(self.x)
        list.append(self.y)
        list.append(self.status)
        list.append(self)
        return (list)

    def print_kinds(self):
        print(self.kinds) 

    def print_x(self):
        print(self.x) 

    def print_y(self):
        print(self.y) 

    #def print_status(self):
        #print(self.status)

    def print_color(self):
        print(self.color)

    def print_all(self):
        print(self.kinds) 
        print(self.x) 
        print(self.y) 
        print(self.status)
        print(self.color)
