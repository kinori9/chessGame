from global_var import *
from location_cal import *

def get_pawn_list(x, y, color):
    black = 1
    plus = 1
    minus = -1
    can_move_list = []
    not_found = True
    #print('white_piece.items() : {}\n black_piece', white_piece, black_piece)
    if color == 'white':
        if y == 6: #예외 처리 맨처음 두칸 갈수 있을경우 
            for i in range(1, 3):
                for name, piece in black_piece.items():
                    if piece.x == x and piece.y == y - i:
                        not_found = False
                if not_found == True:
                    can_move_list.append(str(x) + ',' + str(y - i))
                else:
                    break
                for name, piece in white_piece.items():
                    if piece.x == x and piece.y == y - i:
                        not_found = False
                if not_found == True:
                    can_move_list.append(str(x) + ',' + str(y - i))
                else:
                    break
        else:
            for i in range(1, 2):
                for name, piece in black_piece.items():
                    if piece.x == x and piece.y == y - i:
                        not_found = False
                if not_found == True:
                    can_move_list.append(str(x) + ',' + str(y - i))
                else:
                    break
                for name, piece in white_piece.items():
                    if piece.x == x and piece.y == y - i:
                        not_found = False
                if not_found == True:
                    can_move_list.append(str(x) + ',' + str(y - i))
                else:
                    break
    else: # if color == 'black':
        if y == 1:
            for i in range(1, 3):
                for name, piece in white_piece.items():
                    if piece.x == x and piece.y == y + i:
                        not_found = False
                if not_found == True:
                    can_move_list.append(str(x) + ',' + str(y + i))
                else:
                    break
            for i in range(1, 3):
                for name, piece in black_piece.items():
                    if piece.x == x and piece.y == y + i:
                        not_found = False
                if not_found == True:
                    can_move_list.append(str(x) + ',' + str(y + i))
                else:
                    break
        else:
            for i in range(1, 2):
                for name, piece in white_piece.items():
                    if piece.x == x and piece.y == y + i:
                        not_found = False
                    break
                if not_found == True:
                    can_move_list.append(str(x) + ',' + str(y + i))
                else:
                    break
            for i in range(1, 2):
                for name, piece in black_piece.items():
                    if piece.x == x and piece.y == y + i:
                        not_found = False
                    break
                if not_found == True:
                    can_move_list.append(str(x) + ',' + str(y + i))
                else:
                    break
    return (can_move_list)
