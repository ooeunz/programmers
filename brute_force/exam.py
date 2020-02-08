from collections import deque
from itertools import cycle

def solution(answers):
    FIRST = [1 ,2, 3, 4, 5]
    SECOND = [2, 1, 2, 3, 2, 4, 2, 5]
    THIRD = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]
    score = [0, 0, 0]

    for f, s, t, ans in zip(cycle(FIRST), cycle(SECOND), cycle(THIRD), answers):
        if f == ans: score[0] += 1
        if s == ans: score[1] += 1
        if t == ans: score[2] += 1

    top_score = max(score)

    ans = []
    for idx, value in enumerate(score):
        if value == top_score:
            ans.append(idx+1)

    return ans

if __name__ == "__main__":
    print(solution([1,2,3,4,5]))
