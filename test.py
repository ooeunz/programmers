def solution(budgets, M):
    start = 0
    end = M
    mid = (start + end) // 2

    max_budget = max(budgets)

    while True:
        m = sum(budget if budget <= mid else mid for budget in budgets)
        delta = sum(1 if budget > mid else 0 for budget in budgets)

        if M - delta < m <= M:
            break
        elif m > M:
            end = mid
        else:
            if mid > max_budget:
                return max_budget
            start = mid
        mid = (start + end) // 2

    return mid

print(solution([120, 110, 140, 150], 485))
print(solution([120, 110, 140, 150], 1000))