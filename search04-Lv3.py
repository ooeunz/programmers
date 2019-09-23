# 예산_탐색
def solution(budgets, M):
    lower_bound = 1
    upper_bound = M
    max_budget = max(budgets)

    while True:
        mid = (lower_bound + upper_bound) // 2
        cal = sum(min(mid, budget) for budget in budgets)
        n = len([budget for budget in budgets if budget >= mid])

        if M - n < cal and cal <= M:
            break
        elif M > cal:   #  M - cal >= 0:
            if mid > max_budget:
                return max_budget
            lower_bound = mid
        else:
            upper_bound = mid
    return mid
        
if __name__ == "__main__":
    print(solution([120, 110, 140, 150], 485))