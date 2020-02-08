import collections
from functools import reduce

def multiply(lst: list):
    return reduce(lambda x, y: x * y, lst)

def solution(clothes: list):
    
    ONE_CLOTH = len(clothes)

    category_lst = list(map(lambda x: x[1], clothes))
    if len(set(category_lst)) == 1:
        return ONE_CLOTH


    clothes_cnt = collections.Counter(category_lst)
    clothes_lst = list(clothes_cnt.values())
    OTHERT_CLOTH = multiply(clothes_lst)

    return ONE_CLOTH + OTHERT_CLOTH


if __name__ == "__main__":
    print(solution([["yellow_hat", "headgear"], ["blue_sunglasses", "eyewear"], ["green_turban", "headgear"]]))