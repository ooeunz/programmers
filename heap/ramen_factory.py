import heapq
from collections import deque

def solution(stock: int, dates: list, supplies: list, K: int):
    dates = deque(dates)
    supplies = deque(supplies)
    heap = []
    cnt = 0

    while stock < K:
        while dates and dates[0] <= stock:
            dates.popleft()
            heapq.heappush(heap, -supplies.popleft())

        stock -= heapq.heappop(heap)
        cnt += 1
    return cnt

if __name__ == "__main__":
    print(solution(4, [4, 10, 15], [20, 5, 10], 30))    # 2