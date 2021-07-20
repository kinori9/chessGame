from global_var import *
from location_cal import *

def get_rook_list(x, y, color):
    can_move_list = []
    black = 1
    plus = 1
    minius = -1
    # left, top, right, bottom
    print(color)
    if color == 'white':
        print('############################debug############################')
        # UP
        not_found = True
        kill = False
        for i in range(1, 8):
            print(i)
            for w_name, w_piece in white_piece.items():
                for b_name, b_piece in black_piece.items():
                    if w_piece.x == x and w_piece.y == y - i:
                        not_found = False
                    if (b_piece.x == x and b_piece.y == y - i) and kill == False:
                        can_move_list.append(str(x) + ',' + str(y - i))
                        kill = True
                        not_found = False
            if not_found == True:
                can_move_list.append(str(x) + ',' + str(y - i))
                print('get_rook_list x : {}, y : {}'.format(x, y - i))
            else:
                break
        # DOWN
        print("@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@")
        print('don\' start')
        not_found = True
        kill = False
        for i in range(1, 8):
            print('debug')
            for w_name, w_piece in white_piece.items():
                print('debug2')
                for b_name, b_piece in black_piece.items():
                    print('debug3')
                    if w_piece.x == x and w_piece.y == y + i:
                        not_found = False
                    if (b_piece.x == x and b_piece.y == y + i) and kill == False:
                        can_move_list.append(str(x) + ',' + str(y + i))
                        kill = True
                        not_found = False
            if not_found == True:
                can_move_list.append(str(x) + ',' + str(y + i))
                print('get_rook_list x : {}, y : {}'.format(x, y + i))
            else:
                break

        print('############################debug############################')
        not_found = True
        kill = False
        for i in range(1, 8):
            print(i)
            for w_name, w_piece in white_piece.items():
                for b_name, b_piece in black_piece.items():
                    if w_piece.x == x - i and w_piece.y == y:
                        not_found = False
                    if (b_piece.x == x - i and b_piece.y == y) and kill == False:
                        can_move_list.append(str(x - i) + ',' + str(y))
                        kill = True
                        not_found = False
            if not_found == True:
                can_move_list.append(str(x - i) + ',' + str(y))
                print('get_rook_list x : {}, y : {}'.format(x - i, y))
            else:
                break

        print('############################debug############################')
        not_found = True
        kill = False
        for i in range(1, 8):
            print(i)
            for w_name, w_piece in white_piece.items():
                for b_name, b_piece in black_piece.items():
                    if w_piece.x == x + i and w_piece.y == y:
                        not_found = False
                    if (b_piece.x == x + i and b_piece.y == y) and kill == False:
                        can_move_list.append(str(x + i) + ',' + str(y))
                        kill = True
                        not_found = False
            if not_found == True:
                can_move_list.append(str(x + i) + ',' + str(y))
                print('get_rook_list x : {}, y : {}'.format(x + i, y))
            else:
                break

        """
        kill = False
        #left
        for i in range(0, x, -1):
            for name, piece in white_piece.items():
                if piece.x == x - i and piece.y == y:
                    not_found = False
            if not_found == True:
                can_move_list.append(str(x - i) + ',' + str(y))
            else:
                break
        #top
        #right
        for i in range(x, 8, 1):
            print(i)
            for name, piece in white_piece.items():
                if piece.x != x and piece.y != y:
                    can_move_list.append(str(x + i) + ',' + str(y))
                elif (piece.x == x and piece.y == y) and kill == 0:
                    can_move_list.append(str(x + i) + ',' + str(y))
                    break
        #bottom
        for i in range(y, 8, 1):
            print(i)
            for name, piece in white_piece.items():
                if piece.x != x and piece.y != y:
                    can_move_list.append(str(x) + ',' + str(y - i))
                elif piece.x == x and piece.y == y:
                    can_move_list.append(str(x) + ',' + str(y - i))
                    break

    else: # color == black
        kill = 0
        for i in range(0, x, -1):
            print(i)
            for name, piece in black_piece.items():
                if kill == 1:
                    break
                if piece.x != x and piece.y != y:
                    can_move_list.append(str(x - i) + ',' + str(y))
                elif (piece.x == x and piece.y == y) and kill == 0:
                    can_move_list.append(str(x - i) + ',' + str(y))
                    kill = 1
        #top
        kill = 0
        for i in range(0, y, -1):
            print(i)
            for name, piece in black_piece.items():
                if kill == 1:
                    break
                if piece.x != x and piece.y != y:
                    can_move_list.append(str(x) + ',' + str(y - i))
                elif (piece.x == x and piece.y == y) and kill == 0:
                    can_move_list.append(str(x) + ',' + str(y - i))
                    kill = 1
        #right
        kill = 0
        for i in range(x, 8, 1):
            print(i)
            for name, piece in black_piece.items():
                if kill == 1:
                    break
                if piece.x != x and piece.y != y:
                    can_move_list.append(str(x + i) + ',' + str(y))
                elif (piece.x == x and piece.y == y) and kill == 0:
                    can_move_list.append(str(x + i) + ',' + str(y))
                    kill = 1
        #bottom
        kill = 0
        for i in range(y, 8, 1):
            print(i)
            for name, piece in black_piece.items():
                if kill == 1:
                    break
                if piece.x != x and piece.y != y:
                    can_move_list.append(str(x) + ',' + str(y - i))
                elif (piece.x == x and piece.y == y) and kill == 0:
                    can_move_list.append(str(x) + ',' + str(y - i))
                    kill = 1
        """
    return (can_move_list)
