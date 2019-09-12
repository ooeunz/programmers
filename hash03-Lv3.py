# 빙고
def countBingo(height, width, grid):
    count = 0
    for h in range(height):
        for w in range(width):
            if grid[h][w] == False:
                break
            if w == width-1 and grid[h][w] == True:
                count += 1
    for w in range(width):
        for h in range(height):
            if grid[h][w] == False:
                break
            if h == height-1 and grid[h][w] == True:
                count += 1
    
    w = 0
    for h in range(height):
        if grid[h][w] == False:
            break
        if w == width-1 and grid[h][w] == True:
            count += 1
        w += 1
    w = width-1

    for h in range(height):
        if grid[h][w] == False:
            break
        if h == height-1 and grid[h][w] == True:
                count += 1
        w -= 1
    return count



def solution(board, nums):
    # initialization
    board = [{i:False for i in line} for line in board]

    # check on bingo
    while nums:
        check = nums.pop()
        for index, value in enumerate(board):
            if check in value:
                board[index][check] = True

    grid = list(map(lambda x: list(x.values()), board))
    height = len(grid)  # 세로
    width = len(grid[0])    # 가로

    return countBingo(height, width, grid)
if __name__ == "__main__":
    print(solution([[11, 13, 15, 16], [12, 1, 4, 3], [10, 2, 7, 8], [5, 14, 6, 9]], [14, 3, 2, 4, 13, 1, 16, 11, 5, 15]))