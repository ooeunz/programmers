# 나머지 한 점
from collections import Counter

def solution(v):
    x_point = [x for x, _ in v]
    y_point = [y for _, y in v]

    x_counter = Counter(x_point)
    y_counter = Counter(y_point)

    ans = []
    x = x_counter.most_common()
    y = y_counter.most_common()
    ans.append(x[-1][0])
    ans.append(y[-1][0])

    return ans
if __name__ == "__main__":
    print(solution([[1, 1], [2, 2], [1, 2]]))
