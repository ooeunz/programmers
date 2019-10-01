# 가장 큰 수
from itertools import permutations
def solution(numbers):
    numbers = list(map(str, numbers))
    numbers.sort(key=lambda x: x*4, reverse=True)
    ans = ''.join(number for number in numbers)
    
    return str(int(ans))
if __name__ == "__main__":
    print(solution([6, 10, 2]))
    print(solution([3, 30, 34, 5, 9]))