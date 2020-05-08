def solution(stones: list, k: int):
    last_min = sum(stones[0:k])

    compare = sum(stones[0:k])
    record = 0

    for i in range(1, len(stones) - k):
        compare -= stones[i - 1]
        compare += stones[i + k - 1]

        if last_min > compare:
            last_min = compare
            record = i

    return max(stones[record : record + k])


if __name__ == "__main__":
    print(solution([2, 4, 5, 3, 2, 1, 4, 2, 5, 1], 3))  # 3
