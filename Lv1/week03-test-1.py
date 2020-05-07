# week03 모의고사-1
import itertools

def primecheck(n):
    if n == 2 or n == 3:
        return 1
    if n % 2 == 0 or n == 1:
        return 0
    for i in range(3, int(n ** 0.5) + 1, 2):
        if n % i == 0:
            return 0
    return 1

def solution(nums):
    lst = set(itertools.combinations(nums, 3))
    lst = list(map(sum, lst))

    ans = sum(map(primecheck, lst))
   
    return ans

if __name__ == "__main__":
    print(solution([1, 2, 3, 4]))
    print(solution([1,2,7,6,4]))