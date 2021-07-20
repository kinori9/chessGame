from global_var import *

def get_kinght_list(x, y, color):
    can_move_list = []
    if color == 'white':
        #Quadrant 1
        not_found_1 = True
        not_found_2 = True
        for name, w_piece in white_piece.items():
            if w_piece.x == x + 1 and w_piece.y == y - 2:
                not_found_1 = False
            if w_piece.x == x + 2 and w_piece.y == y - 1:
                not_found_2 = False
        if not_found_1 == True:
            can_move_list.append(str(x + 1) + ',' + str(y - 2))
        if not_found_2 == True:
            can_move_list.append(str(x + 2) + ',' + str(y - 1))

        #Quadrant 2
        not_found_1 = True
        not_found_2 = True
        for name, w_piece in white_piece.items():
            if w_piece.x == x - 1 and w_piece.y == y - 2:
                not_found_1 = False
            if w_piece.x == x - 2 and w_piece.y == y - 1:
                not_found_2 = False
        if not_found_1 == True:
            can_move_list.append(str(x - 1) + ',' + str(y - 2))
        if not_found_2 == True:
            can_move_list.append(str(x - 2) + ',' + str(y - 1))
        #Quadrant 3
        not_found_1 = True
        not_found_2 = True
        for name, w_piece in white_piece.items():
            if w_piece.x == x - 1 and w_piece.y == y + 2:
                not_found_1 = False
            if w_piece.x == x - 2 and w_piece.y == y + 1:
                not_found_2 = False
        if not_found_1 == True:
            can_move_list.append(str(x - 1) + ',' + str(y + 2))
        if not_found_2 == True:
            can_move_list.append(str(x - 2) + ',' + str(y + 1))
        #Quadrant 4
        not_found_1 = True
        not_found_2 = True
        for name, w_piece in white_piece.items():
            if w_piece.x == x + 1 and w_piece.y == y + 2:
                not_found_1 = False
            if w_piece.x == x + 2 and w_piece.y == y + 1:
                not_found_2 = False
        if not_found_1 == True:
            can_move_list.append(str(x + 1) + ',' + str(y + 2))
        if not_found_2 == True:
            can_move_list.append(str(x + 2) + ',' + str(y + 1))
    else:# color == 'black':
        #Quadrant 1
        not_found_1 = True
        not_found_2 = True
        for name, b_piece in black_piece.items():
            if b_piece.x == x + 1 and b_piece.y == y - 2:
                not_found_1 = False
            if b_piece.x == x + 2 and b_piece.y == y - 1:
                not_found_2 = False
        if not_found_1 == True:
            can_move_list.append(str(x + 1) + ',' + str(y - 2))
        if not_found_2 == True:
            can_move_list.append(str(x + 2) + ',' + str(y - 1))

        #Quadrant 2
        not_found_1 = True
        not_found_2 = True
        for name, b_piece in black_piece.items():
            if b_piece.x == x - 1 and b_piece.y == y - 2:
                not_found_1 = False
            if b_piece.x == x - 2 and b_piece.y == y - 1:
                not_found_2 = False
        if not_found_1 == True:
            can_move_list.append(str(x - 1) + ',' + str(y - 2))
        if not_found_2 == True:
            can_move_list.append(str(x - 2) + ',' + str(y - 1))
        #Quadrant 3
        not_found_1 = True
        not_found_2 = True
        for name, b_piece in black_piece.items():
            if b_piece.x == x - 1 and b_piece.y == y + 2:
                not_found_1 = False
            if b_piece.x == x - 2 and b_piece.y == y + 1:
                not_found_2 = False
        if not_found_1 == True:
            can_move_list.append(str(x - 1) + ',' + str(y + 2))
        if not_found_2 == True:
            can_move_list.append(str(x - 2) + ',' + str(y + 1))
        #Quadrant 4
        not_found_1 = True
        not_found_2 = True
        for name, b_piece in black_piece.items():
            if b_piece.x == x + 1 and b_piece.y == y + 2:
                not_found_1 = False
            if b_piece.x == x + 2 and b_piece.y == y + 1:
                not_found_2 = False
        if not_found_1 == True:
            can_move_list.append(str(x + 1) + ',' + str(y + 2))
        if not_found_2 == True:
            can_move_list.append(str(x + 2) + ',' + str(y + 1))
    return (can_move_list)
