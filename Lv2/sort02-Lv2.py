# 최솟값 만들기
def solution(first, second):
    first.sort()
    second.sort(reverse=True)
    mul = lambda x: x[0] * x[1]
    return sum(list(map(mul, zip(first, second))))
if __name__ == "__main__":
    print(solution([1, 4, 2], [5, 4, 4]))
