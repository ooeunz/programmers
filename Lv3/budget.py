def cal_budgets(budgets: list, limit: int):
    ans = 0
    for budget in budgets:
        if budget < limit:
            ans += budget
        else:
            ans += limit
    return ans


def solution(budgets, M):
    low, high = 0, max(budgets)
    ans = 0

    while low <= high:
        mid = (high + low) // 2
        result = cal_budgets(budgets, mid)

        if result > M:
            high = mid - 1
        elif result <= M:
            ans = mid
            low = mid + 1

    return ans


if __name__ == "__main__":
    print(solution([120, 110, 140, 150], 485))  # 127
