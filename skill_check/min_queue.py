def solution(a, b):
    a.sort()
    b.sort(reverse=True)

    ans = 0
    for _ in range(len(a)):
        ans += a.pop() * b.pop()
    
    return ans

if __name__ == "__main__":
    print(solution([1, 4, 2], [5, 4, 4]))