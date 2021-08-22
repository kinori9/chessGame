from global_var import *

def get_rook_list(x, y, color):
    can_move_list = []
    if color == 'white':
        # UP
        not_found = True
        kill = False
        for i in range(1, 8):
            for w_name, w_piece in white_pieces.items():
                for b_name, b_piece in black_pieces.items():
                    if w_piece.x == x and w_piece.y == y - i:
                        not_found = False
                    if (b_piece.x == x and b_piece.y == y - i) and kill == False:
                        can_move_list.append(str(x) + ',' + str(y - i))
                        kill = True
                        not_found = False
            if not_found == True:
                can_move_list.append(str(x) + ',' + str(y - i))
            else:
                break
        # DOWN
        not_found = True
        kill = False
        for i in range(1, 8):
            for w_name, w_piece in white_pieces.items():
                for b_name, b_piece in black_pieces.items():
                    if w_piece.x == x and w_piece.y == y + i:
                        not_found = False
                    if (b_piece.x == x and b_piece.y == y + i) and kill == False:
                        can_move_list.append(str(x) + ',' + str(y + i))
                        kill = True
                        not_found = False
            if not_found == True:
                can_move_list.append(str(x) + ',' + str(y + i))
            else:
                break
        # LEFT
        not_found = True
        kill = False
        for i in range(1, 8):
            for w_name, w_piece in white_pieces.items():
                for b_name, b_piece in black_pieces.items():
                    if w_piece.x == x - i and w_piece.y == y:
                        not_found = False
                    if (b_piece.x == x - i and b_piece.y == y) and kill == False:
                        can_move_list.append(str(x - i) + ',' + str(y))
                        kill = True
                        not_found = False
            if not_found == True:
                can_move_list.append(str(x - i) + ',' + str(y))
            else:
                break
        # RIGHT
        not_found = True
        kill = False
        for i in range(1, 8):
            for w_name, w_piece in white_pieces.items():
                for b_name, b_piece in black_pieces.items():
                    if w_piece.x == x + i and w_piece.y == y:
                        not_found = False
                    if (b_piece.x == x + i and b_piece.y == y) and kill == False:
                        can_move_list.append(str(x + i) + ',' + str(y))
                        kill = True
                        not_found = False
            if not_found == True:
                can_move_list.append(str(x + i) + ',' + str(y))
            else:
                break
    else:
        # DOWN
        not_found = True
        kill = False
        for i in range(1, 8):
            for b_name, b_piece in black_pieces.items():
                for w_name, w_piece in white_pieces.items():
                    if b_piece.x == x and b_piece.y == y + i:
                        not_found = False
                    if (w_piece.x == x and w_piece.y == y + i) and kill == False:
                        can_move_list.append(str(x) + ',' + str(y + i))
                        kill = True
                        not_found = False
            if not_found == True:
                can_move_list.append(str(x) + ',' + str(y + i))
            else:
                break
        # UP
        not_found = True
        kill = False
        for i in range(1, 8):
            for b_name, b_piece in black_pieces.items():
                for w_name, w_piece in white_pieces.items():
                    if b_piece.x == x and b_piece.y == y - i:
                        not_found = False
                    if (w_piece.x == x and w_piece.y == y - i) and kill == False:
                        can_move_list.append(str(x) + ',' + str(y - i))
                        kill = True
                        not_found = False
            if not_found == True:
                can_move_list.append(str(x) + ',' + str(y - i))
            else:
                break
        # LEFT
        not_found = True
        kill = False
        for i in range(1, 8):
            for b_name, b_piece in black_pieces.items():
                for w_name, w_piece in white_pieces.items():
                    if b_piece.x == x - i and b_piece.y == y:
                        not_found = False
                    if (w_piece.x == x - i and w_piece.y == y) and kill == False:
                        can_move_list.append(str(x - i) + ',' + str(y))
                        kill = True
                        not_found = False
            if not_found == True:
                can_move_list.append(str(x - i) + ',' + str(y))
            else:
                break
        # RIGHT
        not_found = True
        kill = False
        for i in range(1, 8):
            for b_name, b_piece in black_pieces.items():
                for w_name, w_piece in white_pieces.items():
                    if b_piece.x == x + i and b_piece.y == y:
                        not_found = False
                    if (w_piece.x == x + i and w_piece.y == y) and kill == False:
                        can_move_list.append(str(x + i) + ',' + str(y))
                        kill = True
                        not_found = False
            if not_found == True:
                can_move_list.append(str(x + i) + ',' + str(y))
            else:
                break
    return (can_move_list)
