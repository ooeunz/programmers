# 예산_탐색
import bisect
def solution(budgets, M):
    budgets.sort()
    MAX = 1000000000
    min = M // len(budgets)
    max_budget = M

    for limit in range(min, MAX):
        num = bisect.bisect_right(budgets, limit)
        max_budget -= limit * (len(budgets) - num)
        max_budget -= sum([budgets[n] for n in range(num)])
        if max_budget < 0:
            return limit-1
        else:
            max_budget = M
        
if __name__ == "__main__":
    print(solution([120, 110, 140, 150], 485))