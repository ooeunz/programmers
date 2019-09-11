# 기능개발
from collections import deque
progresses = [93,30,55]
speeds = [1,30,5]

def solution(progresses, speeds):
    progress = deque(progresses)
    speed = deque(speeds)
    count = 0
    answer = []

    while progress:
        for num in range(len(progress)):
            progress[num] += speed[num]

        # for i, j in zip(progress, speeds):
        #     i += j
        
        
        while progress[0] >= 100:
            progress.popleft()
            speed.popleft()
            count += 1
            if not progress:
                break;
        if count:
            answer.append(count)
            count = 0

    return answer

if __name__ == "__main__":

    print(solution(progresses, speeds))