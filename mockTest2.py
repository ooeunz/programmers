import heapq

works = [1, 1]
n = 3

def solution(n, works):
    works = [-work for work in works]
    heapq.heapify(works)

    if n>= sum(works):
        return 0

    while n:
        check = heapq.heappop(works)
        check += 1
        n -= 1
        heapq.heappush(works, check)
    works = [abs(work) for work in works]
    
    return sum([work ** 2 for work in works])

if __name__ == "__main__":
    print(solution(n, works))