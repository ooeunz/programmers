# 빙고
def countBingo(grid):
    count = 0
    for line in grid:
        if False not in line:
            count += 1
    reverse = list(map(list, zip(*grid)))   # unpacking

    for line in reverse:
        if False not in line:
            count += 1

    length = len(grid)
    w = 0
    for h in range(length):
        if grid[h][w] == False:
            break
        if w == length-1 and grid[h][w] == True:
            count += 1
        w += 1
    w = length-1
    for h in range(length):
        if grid[h][w] == False:
            break
        if h == length-1 and grid[h][w] == True:
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
                break

    grid = list(map(lambda x: list(x.values()), board))

    return countBingo(grid)
if __name__ == "__main__":
    print(solution([[11, 13, 15, 16], [12, 1, 4, 3], [10, 2, 7, 8], [5, 14, 6, 9]], [14, 3, 2, 4, 13, 1, 16, 11, 5, 15]))