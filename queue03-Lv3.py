# FloodFill
from collections import deque
n = 2   # 세로
m = 3   # 가로
image = [[1, 2, 3], [3, 2, 1]]

def initialization(a, b, image, check):
    if a >= len(image) or b >= len(image[0]):
        return True
    elif a < 0 or b < 0:
        return True
    elif check[a][b] == True:
        return True

def floodfill (n, m, image, check, target):
    # If target-color is equal to replacement-color, return.
    if check[n][m] == True:
        return 0
    else:
        queue = deque()
        queue.append(n)
        queue.append(m)

        while queue:
            a = queue.popleft()
            b = queue.popleft()
            
            # up
            if initialization(a-1, b, image, check):
                pass
            elif image[a-1][b] == target:
                check[a-1][b] = True
                queue.append(a-1)
                queue.append(b)

            # down
            if initialization(a+1, b, image, check):
                pass
            elif image[a+1][b] == target:
                check[a+1][b] = True
                queue.append(a+1)
                queue.append(b)
            
            # left
            if initialization(a, b-1, image, check):
                pass
            elif image[a][b-1] == target:
                check[a][b-1] = True
                queue.append(a)
                queue.append(b-1)

            # right
            if initialization(a, b+1, image, check):
                pass
            elif image[a][b+1] == target:
                check[a][b+1] = True
                queue.append(a)
                queue.append(b+1)
        return 1

def solution(n, m, image):
    check = [[False for x in range(m)] for y in range(n)]
    ans = 0
    for y in range(n):
        for x in range(m):
            ans += floodfill(y, x, image, check, image[y][x])
    return ans
    
if __name__ == "__main__":
    print(solution(n, m, image))

