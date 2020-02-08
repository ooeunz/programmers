from collections import Counter
from functools import reduce


def multiply(arr):
    return reduce(lambda x, y: x * y, arr)

def solution(clothes):
    ONE_CLOTH = len(clothes)

    lst = {}
    for cloth in clothes:
        lst[cloth[1]] = 0
    for cloth in clothes:
        lst[cloth[1]] += 1

    other_clothes = []
    for idx in lst:
        other_clothes.append(lst[idx])

    if len(other_clothes) == 1:
        return ONE_CLOTH

    # print(other_clothes)

    return multiply(other_clothes) + ONE_CLOTH
    

if __name__ == "__main__":
    print(solution([["yellow_hat", "headgear"], ["blue_sunglasses", "eyewear"], ["green_turban", "headgear"]])) # 5
    print(solution([["crow_mask", "face"], ["blue_sunglasses", "face"], ["smoky_makeup", "face"]])) # 3