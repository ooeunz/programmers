# 빙고-2
# review

def solution(board, nums):
    # initialization
    length = len(board)
    row_bingo_counts = [0] * length
    col_bingo_counts  = [0] * length
    diagonal_bingo_counts = [0]*2
    ans = 0
    nums = set(nums)


    # check_bingo
    for i, row in enumerate(board):
        for j, number in enumerate(row):
            if number in nums:
                row_bingo_counts[i] += 1
                col_bingo_counts[j] += 1
                if  i == j:
                    diagonal_bingo_counts[0] += 1
                if i + j == length-1:
                    diagonal_bingo_counts[1] += 1

    # debug
    # print(row_bingo_counts)
    # print(col_bingo_counts)
    # print(diagonal_bingo_counts)

    ans += row_bingo_counts.count(length)
    ans += col_bingo_counts.count(length)
    ans += diagonal_bingo_counts.count(length)

    return ans

if __name__ == "__main__":
    print(solution([[11, 13, 15, 16], [12, 1, 4, 3], [10, 2, 7, 8], [5, 14, 6, 9]], [14, 3, 2, 4, 13, 1, 16, 11, 5, 15]))