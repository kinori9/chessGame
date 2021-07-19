from global_var import *
from location_cal import *

def get_rook_list(x, y, color):
    can_move_list = []
    black = 1
    plus = 1
    minius = -1
    # left, top, right, bottom
    """
    if color == 'white':
        if y == 6: #예외 처리 맨처음 두칸 갈수 있을경우 
            kill = False
            for i in range(1, 3): for name, piece in white_piece.items():
                    if piece.x == x and piece.y == y - i:
                        not_found = False
                        if piece.color != color:
                            kill = True
                if kill == True:
                    can_move_list.append(str(x) + ',' + str(y - i))
                    break
                if not_found == True:
                    can_move_list.append(str(x) + ',' + str(y - i))
                else:
                    break
        else:
            kill = False
            for i in range(1, 2):
                for name, piece in white_piece.items():
                    if piece.x == x and piece.y == y - i:
                        not_found = False
                        if piece.color != color:
                            kill = True
                if kill == True:
                    can_move_list.append(str(x) + ',' + str(y - i))
                    break
                if not_found == True:
                    can_move_list.append(str(x) + ',' + str(y - i))
                else:
                    break
    else: # if color == 'black':
        if y == 1:
            kill = False
            for i in range(1, 3):
                for name, piece in black_piece.items():
                    if piece.x == x and piece.y == y + i:
                        not_found = False
                        if piece.color != color:
                            kill = True
                if kill == True:
                    can_move_list.append(str(x) + ',' + str(y + i))
                    break
                else:
                    can_move_list.append(str(x) + ',' + str(y + i))
                if not_found == True:
                    can_move_list.append(str(x) + ',' + str(y + i))
                else:
                    break
        else:
            kill = False
            for i in range(1, 2):
                for name, piece in black_piece.items():
                    if piece.x == x and piece.y == y + i:
                        not_found = False
                        if piece.color != color:
                            kill = True
                if kill == True:
                    can_move_list.append(str(x) + ',' + str(y + i))
                    break
                else:
                    can_move_list.append(str(x) + ',' + str(y + i))
                if not_found == True:
                    can_move_list.append(str(x) + ',' + str(y + i))
                else:
                    break

    """
    if color == 'white':
        kill = False
        #left
        for i in range(0, x, -1):
            for name, piece in white_piece.items():
                if piece.x == x - i and piece.y == y:
                    not_found = False
            if not_found == True:
                can_move_list.append(location_calc_x(x, i, minius) + ',' + location_calc_y(y, 0, plus))
            else:
                break
        #top
        for i in range(0, y, -1):
            print(i)
            for name, piece in white_piece.items():
                if piece.x != x and piece.y != y:
                    can_move_list.append(str(location_calc_x(x, 0, plus) + ',' + str(location_calc_y(y, i, minius))))
                    total += 1
                elif (piece.x == x and piece.y == y) and kill == 0:
                    can_move_list.append(str(locatoin_calc_x(x, 0, plus) + ',' + str(location_calc_y(y, i, minius))))
                    total += 1
                    break
        #right
        for i in range(x, 8, 1):
            print(i)
            for name, piece in white_piece.items():
                if piece.x != x and piece.y != y:
                    can_move_list.append(str(location_calc_x(x, i, plus) + ',' + str(location_calc_y(y, 0, plus))))
                    total += 1
                elif (piece.x == x and piece.y == y) and kill == 0:
                    can_move_list.append(str(locatoin_calc_x(x, i, plus) + ',' + str(location_calc_y(y, 0, plus))))
                    total += 1
                    break
        #bottom
        for i in range(y, 8, 1):
            print(i)
            for name, piece in white_piece.items():
                if piece.x != x and piece.y != y:
                    can_move_list.append(str(location_calc_x(x, 0, plus) + ',' + str(location_calc_y(y, i, minius))))
                    total += 1
                elif piece.x == x and piece.y == y:
                    can_move_list.append(str(locatoin_calc_x(x, 0, plus) + ',' + str(location_calc_y(y, i, minius))))
                    total += 1
                    break

    else: # color == black
        kill = 0
        for i in range(0, x, -1):
            print(i)
            for name, piece in black_piece.items():
                if kill == 1:
                    break
                if piece.x != x and piece.y != y:
                    can_move_list.append(str(location_calc_x(x, i, minius) + ',' + str(location_calc_y(y, 0, plus))))
                    total += 1
                elif (piece.x == x and piece.y == y) and kill == 0:
                    can_move_list.append(str(locatoin_calc_x(x, i, minius) + ',' + str(location_calc_y(y, 0, plus))))
                    total += 1
                    kill = 1
        #top
        kill = 0
        for i in range(0, y, -1):
            print(i)
            for name, piece in black_piece.items():
                if kill == 1:
                    break
                if piece.x != x and piece.y != y:
                    can_move_list.append(str(location_calc_x(x, 0, plus) + ',' + str(location_calc_y(y, i, minius))))
                    total += 1
                elif (piece.x == x and piece.y == y) and kill == 0:
                    can_move_list.append(str(locatoin_calc_x(x, 0, plus) + ',' + str(location_calc_y(y, i, minius))))
                    total += 1
                    kill = 1
        #right
        kill = 0
        for i in range(x, 8, 1):
            print(i)
            for name, piece in black_piece.items():
                if kill == 1:
                    break
                if piece.x != x and piece.y != y:
                    can_move_list.append(str(location_calc_x(x, i, plus) + ',' + str(location_calc_y(y, 0, plus))))
                    total += 1
                elif (piece.x == x and piece.y == y) and kill == 0:
                    can_move_list.append(str(locatoin_calc_x(x, i, plus) + ',' + str(location_calc_y(y, 0, plus))))
                    total += 1
                    kill = 1
        #bottom
        kill = 0
        for i in range(y, 8, 1):
            print(i)
            for name, piece in black_piece.items():
                if kill == 1:
                    break
                if piece.x != x and piece.y != y:
                    can_move_list.append(str(location_calc_x(x, 0, plus) + ',' + str(location_calc_y(y, i, minius))))
                    total += 1
                elif (piece.x == x and piece.y == y) and kill == 0:
                    can_move_list.append(str(locatoin_calc_x(x, 0, plus) + ',' + str(location_calc_y(y, i, minius))))
                    total += 1
                    kill = 1
