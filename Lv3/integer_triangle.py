def solution(triangle):
    for i in range(len(triangle)-1, 0, -1):
        for j in range(len(triangle[i])-1):
            triangle[i-1][j] = max(triangle[i-1][j] + triangle[i][j], triangle[i-1][j] + triangle[i][j+1])

    return triangle[0][0]

if __name__ == "__main__":
    print(solution([[7], [3, 8], [8, 1, 0], [2, 7, 4, 4], [4, 5, 2, 6, 5]]))    # 30