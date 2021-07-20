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
                for b_name, b_piece in black_piece.items():
                    for w_name, w_piece in white_piece.items():
                        if (w_piece.x == x and w_piece.y == y - i ) or (b_piece.x == x and b_piece.y == y - 1):
                            not_found = False
                if not_found == True:
                    can_move_list.append(str(x) + ',' + str(y - i))
                else:
                    break
        else:
            for i in range(1, 2):
                for b_name, b_piece in black_piece.items():
                    for w_name, w_piece in white_piece.items():
                        if (w_piece.x == x and w_piece.y == y - i) or (b_piece.x == x and b_piece.y == y - 1):
                            not_found = False
                if not_found == True:
                    can_move_list.append(str(x) + ',' + str(y - i))
                else:
                    break
        for name, piece in black_piece.items():
            if piece.x == x - 1 and piece.y == y - 1:
                can_move_list.append(str(x - 1) + ',' + str(y - 1))
            if piece.x == x + 1 and piece.y == y - 1:
                can_move_list.append(str(x + 1) + ',' + str(y - 1))
    else: # if color == 'black':
        if y == 1: #예외 처리맨처음 두칸 가능한 경우:
            for i in range(1, 3):
                for w_name, w_piece in white_piece.items():
                    for b_name, b_piece in black_piece.items():
                        if (b_piece.x == x and b_piece.y == y + i) or (w_piece.x == x and w_piece.y == y + 1):
                            not_found = False
                if not_found == True:
                    can_move_list.append(str(x) + ',' + str(y + i))
                else:
                    break
        else:
            for i in range(1, 2):
                for w_name, w_piece in white_piece.items():
                    for b_name, b_piece in black_piece.items():
                        if (b_piece.x == x and b_piece.y == y + i) or (w_piece.x == x and w_piece.y == y + 1):
                            not_found = False
                if not_found == True:
                    can_move_list.append(str(x) + ',' + str(y + i))
                else:
                    break
        for name, piece in white_piece.items():
            if piece.x == x - 1 and piece.y == y + 1:
                can_move_list.append(str(x - 1) + ',' + str(y + 1))
            if piece.x == x + 1 and piece.y == y + 1:
                can_move_list.append(str(x + 1) + ',' + str(y + 1))
    return (can_move_list)
