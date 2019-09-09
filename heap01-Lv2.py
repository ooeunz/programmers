import heapq
scoville = [1, 2, 3, 9, 10, 12]
K = 7
def solution(scoville, K):
    heapq.heapify(scoville)
    ans = 0
    while scoville[0] <K:
        # make
        first = heapq.heappop(scoville)
        second = heapq.heappop(scoville)
        mix = first + second*2

        # push
        heapq.heappush(scoville, mix)
        ans += 1
    return ans

if __name__ == "__main__":
    print(solution(scoville, K))