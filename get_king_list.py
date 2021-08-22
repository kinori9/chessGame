from global_var import *

def get_king_list(x, y, color):
    can_move_list = []
    if color == 'white':
        not_found_1 = True
        not_found_2 = True
        not_found_3 = True
        not_found_4 = True
        not_found_5 = True
        not_found_6 = True
        not_found_7 = True
        not_found_8 = True
        for name, w_piece in white_pieces.items():
            if w_piece.x == x and w_piece.y == y - 1:
                not_found_1 = False
            if w_piece.x == x + 1 and w_piece.y == y - 1:
                not_found_2 = False
            if w_piece.x == x + 1 and w_piece.y == y:
                not_found_3 = False
            if w_piece.x == x + 1 and w_piece.y == y + 1:
                not_found_4 = False
            if w_piece.x == x and w_piece.y == y + 1:
                not_found_5 = False
            if w_piece.x == x - 1 and w_piece.y == y + 1:
                not_found_6 = False
            if w_piece.x == x - 1 and w_piece.y == y:
                not_found_7 = False
            if w_piece.x == x - 1 and w_piece.y == y - 1:
                not_found_8 = False
        if not_found_1 == True:
            can_move_list.append(str(x) + ',' + str(y - 1))
        if not_found_2 == True:
            can_move_list.append(str(x + 1) + ',' + str(y - 1))
        if not_found_3 == True:
            can_move_list.append(str(x + 1) + ',' + str(y))
        if not_found_4 == True:
            can_move_list.append(str(x + 1) + ',' + str(y + 1))
        if not_found_5 == True:
            can_move_list.append(str(x) + ',' + str(y + 1))
        if not_found_6 == True:
            can_move_list.append(str(x - 1) + ',' + str(y + 1))
        if not_found_7 == True:
            can_move_list.append(str(x - 1) + ',' + str(y))
        if not_found_8 == True:
            can_move_list.append(str(x - 1) + ',' + str(y - 1))
    else:
        not_found_1 = True
        not_found_2 = True
        not_found_3 = True
        not_found_4 = True
        not_found_5 = True
        not_found_6 = True
        not_found_7 = True
        not_found_8 = True
        for name, b_piece in black_pieces.items():
            if b_piece.x == x and b_piece.y == y - 1:
                not_found_1 = False
            if b_piece.x == x + 1 and b_piece.y == y - 1:
                not_found_2 = False
            if b_piece.x == x + 1 and b_piece.y == y:
                not_found_3 = False
            if b_piece.x == x + 1 and b_piece.y == y + 1:
                not_found_4 = False
            if b_piece.x == x and b_piece.y == y + 1:
                not_found_5 = False
            if b_piece.x == x - 1 and b_piece.y == y + 1:
                not_found_6 = False
            if b_piece.x == x - 1 and b_piece.y == y:
                not_found_7 = False
            if b_piece.x == x - 1 and b_piece.y == y - 1:
                not_found_8 = False
        if not_found_1 == True:
            can_move_list.append(str(x) + ',' + str(y - 1))
        if not_found_2 == True:
            can_move_list.append(str(x + 1) + ',' + str(y - 1))
        if not_found_3 == True:
            can_move_list.append(str(x + 1) + ',' + str(y))
        if not_found_4 == True:
            can_move_list.append(str(x + 1) + ',' + str(y + 1))
        if not_found_5 == True:
            can_move_list.append(str(x) + ',' + str(y + 1))
        if not_found_6 == True:
            can_move_list.append(str(x - 1) + ',' + str(y + 1))
        if not_found_7 == True:
            can_move_list.append(str(x - 1) + ',' + str(y))
        if not_found_8 == True:
            can_move_list.append(str(x - 1) + ',' + str(y - 1))
    return (can_move_list)
