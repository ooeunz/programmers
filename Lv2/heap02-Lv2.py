# 배상 비용 최소화
import heapq

def solution(no, works):
    works = [-work for work in works]
    heapq.heapify(works)

    while no:
        check = heapq.heappop(works)
        check += 1
        heapq.heappush(works, check)
        no -= 1
    
    return sum([work ** 2 for work in works])

if __name__ == "__main__":
    print(solution(4, [4, 3, 3]))