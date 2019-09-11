# 나머지 한 점
from collections import Counter

def solution(v):
    x_point = [x for x, _ in v]
    y_point = [y for _, y in v]

    x_counter = dict(Counter(x_point)).items()
    y_counter = dict(Counter(y_point)).items()

    ans = []
    x, _ = min(x_counter, key = lambda x:x[1])
    y, _ = min(y_counter, key = lambda x:x[1])
    ans.append(x)
    ans.append(y)

    return ans
if __name__ == "__main__":
    print(solution([[1, 1], [2, 2], [1, 2]]))
