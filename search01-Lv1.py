# 세 소수의 합
import itertools

def solution(n):
    # initialization
    lst = [i for i in range(2, n)]
    nets = [(4, 2), (6, 3), (10, 5)]
    count = check = 0
    collection = []

    # remove Composite Numbers
    for start, step in nets:
        if start <= n:
            for i in range(start, n, step):
                if i in lst:
                    lst.remove(i)

    # find
    collection.extend(list(itertools.permutations(lst, 3)))
    for i in collection:
        if sum(i) == n:
            count += 1
    return count//6

if __name__ == "__main__":
    print(solution(33))
    print(solution(9))