def solution(n: int, times: list):
    start, end = 1, max(times) * n
    ans = end

    while start <= end:
        mid = (start + end) // 2
        if n > sum(map(lambda x: mid//x, times)):
            start = mid + 1
        else:
            ans = min(mid, ans)
            end = mid - 1
            
    return ans

if __name__ == "__main__":
    print(solution(6, [7, 10]))