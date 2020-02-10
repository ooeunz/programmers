# H-index
def solution(citations):
    citations.sort()
    N = len(citations)
    ans = 0 

    if citations[0] == citations[-1]:
        return citations[0]
    if citations[0]+1 == citations[-1]:
        return citations[0]

    for idx in range(N):
        upper = 0
        lower = 0
        for citation in citations:
            if citation >= idx:
                upper += 1
            elif citation <= idx:
                lower += 1
        if upper and lower:
            if idx <= upper and idx >= lower:
                ans = idx
    if ans == 0:
        return 1
    return ans


if __name__ == "__main__":
    print(solution([3, 0, 6, 1, 5]))
    print(solution([10000, 10000, 10000, 10000, 10000]))
    # print(solution([2, 2, 2, 3]))
    print(solution([20, 19, 19, 1]))
    print(solution([22, 42]))