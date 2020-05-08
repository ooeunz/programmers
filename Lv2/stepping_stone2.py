# 징검 다리
def solution(stones: list, k: int):
    start, end = 0, max(stones)
    ans = 0

    while start <= end:
        mid = (start + end) // 2
        ex_stones = [0 if stones[i] < mid else stones[i] for i in range(len(stones))]
        cnt = 0
        for stone in ex_stones:
            if not stone:
                cnt += 1
        if cnt >= k:
            end = mid - 1
        else:
            ans = mid
            start = mid + 1

    return ans


if __name__ == "__main__":
    print(solution([2, 4, 5, 3, 2, 1, 4, 2, 5, 1], 3))  # 3