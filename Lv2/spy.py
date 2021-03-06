from collections import Counter
from functools import reduce

def solution(clothes):
    cnt = Counter([category for name, category in clothes])
    return reduce(lambda x, y: x*(y+1), cnt.values(), 1) - 1

if __name__ == "__main__":
    print(solution([["yellow_hat", "headgear"], ["blue_sunglasses", "eyewear"], ["green_turban", "headgear"]]))