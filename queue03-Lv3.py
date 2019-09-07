# FloodFill
from collections import deque

n = 2   # 세로
m = 3   # 가로
image = [[1, 2, 3], [3, 2, 1]]

def solution(n, m, image):
    answer = n*m
    convert = []
    width = []

    merge = 0   # 세로로 같은 색의 블럭 수
    check = 30000   # 확인할 블럭 (최초 1회 확인은 무적권 틀림)

    # height
    for i in range(m):
        for j in range(n):
            if image[j][i] == check:
                merge += 1
            elif image[j][i] != check:
                answer -= merge
                merge = 0
            check = image[j][i]
            convert.append(check)
        width.append(list(deque(convert)))  # 리스트 안에 [[deque], [deque]]
        convert.clear()

    # width
    # deque에서 하나씩 pop
    check = 30000
    for i in range(len(width)): # 세로길이
        for j in range(len(width[0])):   # 가로길이
            print("adsf")
            
            
    return answer

if __name__ == "__main__":
    print(solution(n, m, image))