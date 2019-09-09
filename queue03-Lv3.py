# FloodFill
from collections import deque

n = 3   # 세로
m = 3   # 가로
image = [[1, 2, 3], [3, 2, 1], [4, 2, 1]]

def solution(n, m, image):
    answer = n*m
    convert = []
    width = []
    check = 30000   # 확인할 블럭 (최초 1회 확인은 무적권 틀림)

    height = list(map(deque, image))

    # height
    for j in range(len(height[0])):
        for i in range(len(height)):
            if height[i][0] == check:
                answer -= 1
            check = height[i].popleft()
            convert.append(check)
        width.append((deque(convert)))  # 리스트 안에 [[deque], [deque]]
        convert.clear()
        check = 30000

    # width
    check = 30000
    for j in range(len(width[0])):
        for i in range(len(width)):
            if width[i][0] == check:
                answer -= 1
            check = width[i].popleft()
        check = 30000 
    return answer

if __name__ == "__main__":
    print(solution(n, m, image))

