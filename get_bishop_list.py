from global_var import *

def get_bishop_list(x, y, color):
    can_move_list = []
    if color == 'white':
    #Quadrant 1
        not_found = True
        kill = False
        for i in range(1, 8):
            for w_name, w_piece in white_piece.items():
                for b_name, b_piece in black_piece.items():
                    if w_piece.x == x + i and w_piece.y == y - i:
                        not_found = False
                    if (b_piece.x == x + i and b_piece.y == y - i) and kill == False:
                        can_move_list.append(str(x + i) + ',' + str(y - i))
                        kill = True
                        not_found = False
            if not_found == True:
                can_move_list.append(str(x + i) + ',' + str(y - i))
            else:
                break

    #Quadrant 2
        not_found = True
        kill = False
        for i in range(1, 8):
            for w_name, w_piece in white_piece.items():
                for b_name, b_piece in black_piece.items():
                    if w_piece.x == x - i and w_piece.y == y - i:
                        not_found = False
                    if (b_piece.x == x - i and b_piece.y == y - i) and kill == False:
                        can_move_list.append(str(x - i) + ',' + str(y - i))
                        kill = True
                        not_found = False
            if not_found == True:
                can_move_list.append(str(x - i) + ',' + str(y - i))
            else:
                break

    #Quadrant 3
        not_found = True
        kill = False
        for i in range(1, 8):
            for w_name, w_piece in white_piece.items():
                for b_name, b_piece in black_piece.items():
                    if w_piece.x == x - i and w_piece.y == y + i:
                        not_found = False
                    if (b_piece.x == x - i and b_piece.y == y + i) and kill == False:
                        can_move_list.append(str(x - i) + ',' + str(y + i))
                        kill = True
                        not_found = False
            if not_found == True:
                can_move_list.append(str(x - i) + ',' + str(y + i))
            else:
                break

    #Quadrant 4
        not_found = True
        kill = False
        for i in range(1, 8):
            for w_name, w_piece in white_piece.items():
                for b_name, b_piece in black_piece.items():
                    if w_piece.x == x + i and w_piece.y == y + i:
                        not_found = False
                    if (b_piece.x == x + i and b_piece.y == y + i) and kill == False:
                        can_move_list.append(str(x + i) + ',' + str(y + i))
                        kill = True
                        not_found = False
            if not_found == True:
                can_move_list.append(str(x + i) + ',' + str(y + i))
            else:
                break
    else:
    #Quadrant 1
        not_found = True
        kill = False
        for i in range(1, 8):
            for b_name, b_piece in black_piece.items():
                for w_name, w_piece in white_piece.items():
                    if b_piece.x == x + i and b_piece.y == y - i:
                        not_found = False
                    if (w_piece.x == x + i and w_piece.y == y - i) and kill == False:
                        can_move_list.append(str(x + i) + ',' + str(y - i))
                        kill = True
                        not_found = False
            if not_found == True:
                can_move_list.append(str(x + i) + ',' + str(y - i))
            else:
                break

    #Quadrant 2
        not_found = True
        kill = False
        for i in range(1, 8):
            for b_name, b_piece in black_piece.items():
                for w_name, w_piece in white_piece.items():
                    if b_piece.x == x - i and b_piece.y == y - i:
                        not_found = False
                    if (w_piece.x == x - i and w_piece.y == y - i) and kill == False:
                        can_move_list.append(str(x - i) + ',' + str(y - i))
                        kill = True
                        not_found = False
            if not_found == True:
                can_move_list.append(str(x - i) + ',' + str(y - i))
            else:
                break

    #Quadrant 3
        not_found = True
        kill = False
        for i in range(1, 8):
            for b_name, b_piece in black_piece.items():
                for w_name, w_piece in white_piece.items():
                    if b_piece.x == x - i and b_piece.y == y + i:
                        not_found = False
                    if (w_piece.x == x - i and w_piece.y == y + i) and kill == False:
                        can_move_list.append(str(x - i) + ',' + str(y + i))
                        kill = True
                        not_found = False
            if not_found == True:
                can_move_list.append(str(x - i) + ',' + str(y + i))
            else:
                break

    #Quadrant 4
        not_found = True
        kill = False
        for i in range(1, 8):
            for b_name, b_piece in black_piece.items():
                for w_name, w_piece in white_piece.items():
                    if b_piece.x == x + i and b_piece.y == y + i:
                        not_found = False
                    if (w_piece.x == x + i and w_piece.y == y + i) and kill == False:
                        can_move_list.append(str(x + i) + ',' + str(y + i))
                        kill = True
                        not_found = False
            if not_found == True:
                can_move_list.append(str(x + i) + ',' + str(y + i))
            else:
                break
    return (can_move_list)
