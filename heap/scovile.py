import heapq


def solution(scoville, K):
    heapq.heapify(scoville)
    cnt = 0

    while scoville[0] < K:
        if len(scoville) == 1:
            return -1

        fir = heapq.heappop(scoville)
        sec = heapq.heappop(scoville)
        mix = fir + sec * 2

        heapq.heappush(scoville, mix)
        cnt += 1
    return cnt

if __name__ == "__main__":
    print(solution([1, 2, 3, 9, 10, 12], 7))

