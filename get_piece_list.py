from global_var import *

def location_cal(num):
    return (num * 100)

def location_calc_y(y, distance):
    fix_y = 50
    plus = 1
    minus = -1
    if cal == plus:
        return ((y * 100 + fix_y) + (distance * 100))
    else:
        return ((y * 100 + fix_y) - (distance * 100))

def location_calc_x(x, distance, cal):
    fix_x = 10
    plus = 1
    minus = -1
    if cal == plus:
        return ((x * 100 + fix_x) + (distance * 100))
    else:
        return ((x * 100 + fix_x) - (distance * 100))

def get_pawn_list(x, y, kinds):
    white = 0
    black = 1
    plus = 1
    minus = -1
    can_move_list = []
    if kinds == white:
        for piece in white_piece:
            if piece.x != x and piece.y != y:
                can_move_list.append(str(location_calc_x(x)) + ',' + str(location_calc_y(y, 1)))
            if y == 6:
                if piece.x != x and piece.y != y:
                    can_move_list.append(str(location_calc_x(x)) + ',' + str(location_calc_y(y, 2)))
    else:
        for piece in black_piece:
            if piece.x != x and piece.y != y:
                can_move_list.append(str(location_calc_x(x)) + ',' + str(location_calc_y(y, 1)))
        if y == 1:
            for piece in black_piece:
                if piece.x != x and piece.y != y:
                    can_move_list.append(str(location_calc_x(x)) + ',' + str(location_calc_y(y, 2)))


    print(can_move_list)
    return (can_move_list)

#def get_rook_list(x, y):

