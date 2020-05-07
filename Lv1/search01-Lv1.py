# 세 소수의 합
import itertools

def solution(n):
    # initialization
    collection = []
    count = 0
    lst = set(range(2,n+1))

    for i in range(2,n+1):
        if i in lst:
            lst -= set(range(2*i,n+1,i))
    
    # find
    collection.extend(list(itertools.combinations(lst, 3)))
    for i in collection:
        if sum(i) == n:
            count += 1
    return count

if __name__ == "__main__":
    print(solution(33))
    print(solution(9))