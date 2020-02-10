# 기능개발
from collections import deque

def solution(progresses, speeds):
    progress = deque(progresses)
    speed = deque(speeds)
    count = 0
    answer = []

    while progress:
        for num in range(len(progress)):
            progress[num] += speed[num]
        
        while progress[0] >= 100:
            progress.popleft()
            speed.popleft()
            count += 1
            if not progress:
                break
        if count:
            answer.append(count)
            count = 0

    return answer

if __name__ == "__main__":

    print(solution([93,30,55], [1,30,5]))