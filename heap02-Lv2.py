import heapq

no = 4
works = [4, 3, 3]
def solution(no, works):
    last = len(works)-1

    while no:
        works.sort()
        if works[last]:
            works[last] -= 1
        no -= 1
    result  = 0
    for i in works:
        result += i ** 2
    return result

print(solution(no, works))