# 가장 큰 수
from itertools import permutations
def solution(numbers):
    numbers = [str(number) for number in numbers]
    ans = []
    for number in permutations(numbers):
        ans.append(''.join(number))
    
    return max(ans)
if __name__ == "__main__":
    print(solution([6, 10, 2]))
    print(solution([3, 30, 34, 5, 9]))