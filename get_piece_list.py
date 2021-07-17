from global_var import *

def location_cal(num):
    return (num * 100)

def location_calc_y(y, distance, cal):
    fix_y = 50
    plus = 1
    minus = -1
    if cal == plus:
        return (str((y * 100 + fix_y) + (distance * 100)))
    else:
        return (str((y * 100 + fix_y) - (distance * 100)))

def location_calc_x(x, distance, cal):
    fix_x = 10
    plus = 1
    minus = -1
    if cal == plus:
        return (str((x * 100 + fix_x) + (distance * 100)))
    else:
        return (str((x * 100 + fix_x) - (distance * 100)))

def get_pawn_list(x, y, kinds):
    white = 0
    black = 1
    plus = 1
    minus = -1
    can_move_list = []
    not_found = True
    #print('white_piece.items() : {}\n black_piece', white_piece, black_piece)
    # top
    if kinds == white:
        if i == 6:
            for i in range(1, 3):
                for name, piece in white_piece.items():
                    if piece.x == x and piece.y == y + i:
                        not_found = False
                if not_found == True:
                    can_move_list.append(location_calc_x(x, 0, plus) + ',' + location_calc_y(y, i, plus))
                else:
                    break
        else:
            for i in range(1, 2):
                for name, piece in white_piece.items():
                    if piece.x == x and piece.y == y + i:
                        not_found = False
                if not_found == True:
                    can_move_list.append(location_calc_x(x, 0, plus) + ',' + location_calc_y(y, i, plus))
                else:
                    break
    else:
    # down
        for i in range(1, 3):
            for name, piece in black_piece.items():
                if piece.x == x and piece.y == y - i:
                    not_found = False
            if not_found == True:
                can_move_list.append(location_calc_x(x, 0, plus) + ',' + location_calc_y(y, i, minus))
            else:
                break
        else:
            for i in range(1, 2):
                for name, piece in black_piece.items():
                    if piece.x == x and piece.y == y + i:
                        not_found = False
                if not_found == True:
                    can_move_list.append(location_calc_x(x, 0, plus) + ',' + location_calc_y(y, i, plus))
                else:
                    break
    return (can_move_list)

def get_rook_list(x, y, kinds):
    can_move_list = []
    white = 0
    black = 1
    plus = 1
    minius = -1
    # left, top, right, bottom
    if kinds == white:
        #left
        for i in range(0, x, -1):
            for name, piece in white_piece.items():
                if piece.x == x - i and piece.y == y:
                    not_found = False
                if not_found == True:
                    if kill = True:
                        break
                    can_move_list.append(location_calc_x(x, i, minius) + ',' + location_calc_y(y, 0, plus))
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

    else: # kinds == black
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
        if total == 0:
            print('don\'t move')
