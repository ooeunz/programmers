# 게임_맵_최단거리
import copy
def check_bounds(x, y, end):
    if x < 0 or x > end[0]:   
        return True
    if y < 0 or y > end[1]:   
        return True

def find_route(x, y, end, maps, check, count, ans):
    if check_bounds(x, y, end):
        return

    if x == end[0] and y == end[1]:
        count += 1
        ans.append(count)
        return

    if maps[x][y] == True and check[x][y] == False:
        checking = copy.deepcopy(check)
        count += 1
        checking[x][y] = True
        find_route(x+1, y, end, maps, checking, count, ans)
        find_route(x-1, y, end, maps, checking, count, ans)
        find_route(x, y+1, end, maps, checking, count, ans)
        find_route(x, y-1, end, maps, checking, count, ans)
    elif maps[x][y] == False or check[x][y] == True:
        return

def solution(maps):
    ans = []
    check = [[False for col in row] for row in maps]
    end = (len(maps) - 1, len(maps[0]) - 1)
    count = 0
    find_route(0, 0, end, maps, check, count, ans)
    return min(ans) if ans else -1


if __name__ == "__main__":
    print(solution([[1, 0, 1, 1, 1], [1, 0, 1, 0, 1], [1, 0, 1, 1, 1], [1, 1, 1, 0, 1], [0, 0, 0, 0, 1]]))  # 11
    print(solution([[1, 0, 1, 1, 1], [1, 0, 1, 0, 1], [1, 0, 1, 1, 1], [1, 1, 1, 0, 0], [0, 0, 0, 0, 1]]))  # -1
