# 방문 길이
def can(xy_next, move_x, move_y):
    x = xy_next[0] + move_x
    y = xy_next[1] + move_y
    if x <= 0 or x > 11:   
        return True
    if y <= 0 or y > 11:   
        return True

def move(xy, xy_next, move_x, move_y, course):
    
    # print("move   : {}".format(xy_next))    #debug
    if can(xy_next, move_x, move_y):    # out of range check
        return False
    xy_next[0] += move_x
    xy_next[1] += move_y
    convert = list(map(str, xy))
    convert_next = list(map(str, xy_next))
    position = "({},{})-({},{})".format(convert[0], convert[1], convert_next[0], convert_next[1])
    position_reverse = "({},{})-({},{})".format(convert_next[0], convert_next[1], convert[0], convert[1])
    xy[0], xy[1] = xy_next

    # print(position) # debug
    if position in course or position_reverse in course:
        return False
    else:
        course[position] = True
        return True

def action(xy, xy_next, move_x, move_y, course):
    # print("action : {}".format(xy_next))   # debug
    if move(xy, xy_next, move_x, move_y, course) == False:
        return 0
    else:
        return 1

def solution(dirs):
    # initialization
    xy = [6, 6]
    xy_next = [6, 6]
    course = {}
    count = 0

    for dir in dirs:
        if dir == "U":
            count += action(xy, xy_next, 0, -1, course)
        elif dir == "D":
            count += action(xy, xy_next, 0, 1, course)
        elif dir == "R":
            count += action(xy, xy_next, 1, 0, course)
        elif dir == "L":
            count += action(xy, xy_next, -1, 0, course)
    return count

            

if __name__ == "__main__":
    print(solution("ULURRDLLU"))
    print(solution("LULLLLLLU"))
        





