# 더 맵게
import heapq

def solution(scoville, K):
    heapq.heapify(scoville)
    ans = 0
    if len(scoville) <= 1:
        return -1
    else:
        while scoville[0] <K:
            if len(scoville) <= 1:
                return -1
            # make
            first = heapq.heappop(scoville)
            second = heapq.heappop(scoville)
            mix = first + second*2

            # push
            heapq.heappush(scoville, mix)
            ans += 1
    return ans

if __name__ == "__main__":
    print(solution([1, 2, 3, 9, 10, 12], 7))