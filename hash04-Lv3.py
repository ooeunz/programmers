# 방문 길이
def can(x, y):
    if x < 0 or x >10:
        return True
    elif y < 0 or y> 10:
        return True

def move(x, y, room):
    if room[y][x] == True:     # 갔던 길이라면
        return 0
    elif room[y][x] == False:    # 처음가는 길이라면
        room[y][x] = True
        return 1

def solution(dirs):
    # initialization
    room = [[False for w in range(11)]for h in range(11)]
    person = {"x" : 5, "y" : 5}
    room[5][5] = True
    distance = 0

    for dir in dirs:
        if dir == "U":
            person["y"] -= 1
            if can(person["x"], person["y"]):
                continue
            else:
                distance += move(person["x"], person["y"], room)
        elif dir == "D":
            person["y"] += 1
            if can(person["x"], person["y"]):
                continue
            else:
                distance += move(person["x"], person["y"], room)
        elif dir == "L":
            person["x"] -= 1
            if can(person["x"], person["y"]):
                continue
            else:
                distance += move(person["x"], person["y"], room)
        elif dir == "R":
            person["x"] += 1
            if can(person["x"], person["y"]):
                continue
            else:
                distance += move(person["x"], person["y"], room)
    return distance

if __name__ == "__main__":
    print(solution("ULURRDLLU"))
    print(solution("LULLLLLLU"))
        





