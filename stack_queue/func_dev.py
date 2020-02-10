from collections import deque
import copy


def solution(progresses, speeds):
    progresses = deque(progresses)
    speeds = deque(speeds)
    ans = []
    
    while progresses:
        for i in range(len(progresses)):
            progresses[i] += speeds[i]

        cnt = 0
        while progresses[0] >= 100:
            progresses.popleft()
            speeds.popleft()
            cnt += 1

            if not progresses:
                break
        if cnt:
            ans.append(cnt)
    return ans

if __name__ == "__main__":
    print(solution([93,30,55], [1,30,5]))   # [2, 1]
    print(solution([5,5,5], [21,25,20]))   # [3]
