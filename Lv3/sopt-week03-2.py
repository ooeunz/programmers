# 탑
def solution(heights):
    record = [0 for _ in range(len(heights))]
    N = len(heights)-1

    for start in range(N, 0, -1):
        for end in range(start-1, -1, -1):
            if heights[start] < heights[end]:
                record[start] = end+1
                break
    return record

if __name__ == "__main__":
    print(solution([6, 9, 5, 7, 4]))    # [0,0,2,2,4]
    print(solution([3, 9, 9, 3, 5, 7, 2]))  # [0,0,0,3,3,3,6]
    print(solution([1,5,3,6,7,6,5]))   # [0,0,2,0,0,5,6]