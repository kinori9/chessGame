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
