import heapq
from collections import deque


def cal_ave(begin: int, end_time: int):
    return end_time - begin

def solution(jobs):
    time = 0
    heap = []
    ans = []

    N = len(jobs)
    jobs = deque(sorted(jobs))

    for _ in range(len(jobs)):
        while jobs and jobs[0][0] <= time:
            begin, work = jobs.popleft()
            heapq.heappush(heap, (work, begin))
        
        if not heap:
            begin, work = jobs.popleft()
            heapq.heappush(heap, (work, begin))
        
        working, begin = heapq.heappop(heap)

        if begin > time:
            time = begin + working
        else:
            time += working

        ans.append(cal_ave(begin, time))
    
    return sum(ans) // N

if __name__ == "__main__":
    print(solution([[0, 3], [1, 9], [2, 6]]))   # 9
    print(solution([[24, 10], [18, 39], [34, 20], [37, 5], [47, 22], [20, 47], [15, 2], [15, 34], [35, 43], [26, 1]]))  # 74
    print(solution([[0,1],[0,2],[2,1]]))    # 2
    print(solution([[0, 5], [1, 2], [5, 5]]))   # 6
    print(solution([[0, 3], [1, 9], [500, 6]])) # 6