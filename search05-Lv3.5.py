# 게임_맵_최단거리
# 다시 과거로 돌아와 경로를 재 탐색할 경우 checking이 초기화가 안되고 있음
# Test case-2 번은 적팀진영을 찾을 수 없음에도 똑같이 경로를 탐색한다.
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
        checking = check[:]
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
    return ans


if __name__ == "__main__":
    print(solution([[1, 0, 1, 1, 1], [1, 0, 1, 0, 1], [1, 0, 1, 1, 1], [1, 1, 1, 0, 1], [0, 0, 0, 0, 1]]))  # 11
    print(solution([[1, 0, 1, 1, 1], [1, 0, 1, 0, 1], [1, 0, 1, 1, 1], [1, 1, 1, 0, 1], [0, 0, 0, 0, 1]]))  # -1
