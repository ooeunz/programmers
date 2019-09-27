# 예산_소팅
def solution(departments, budget):
    departments.sort()
    count = 0
    for department in departments: 
        budget -= department
        if budget < 0:
            return count
        else:
            count += 1
    return len(departments)

if __name__ == "__main__":
    print(solution([1,3,2,5,4], 9))
    print(solution([2,2,3,3], 10))