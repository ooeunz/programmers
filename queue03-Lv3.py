# FloodFill
n = 2   # 세로
m = 3   # 가로
image = [[1, 2, 3], [3, 2, 1]]

def floodfill(image, check,  x, y, target):
    if x >= len(image) or y >= len(image[0]):
        return
    elif x < 0 or y < 0:
        return
    else:
        if check[x][y] == True:
            return 0
        elif check[x][y] == False:
            if image[x][y] == target:
                check[x][y] = True
                floodfill(image, check, x+1, y, target)
                floodfill(image, check, x-1, y, target)
                floodfill(image, check, x, y+1, target)
                floodfill(image, check, x, y-1, target)
                return 1
            return 0
    
        
def solution(n, m, image):
    # check 2xlist
    check = [[False for x in range(m)] for y in range(n)]

    ans = 0
    for height in range(n):
        for width in range(m):
            ans += floodfill(image, check, height, width, image[height][width])
    return ans
    
if __name__ == "__main__":
    print(solution(n, m, image))

