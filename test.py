from itertools import permutations

def solution(numbers):
    lst = list(set(map(int, map(''.join, permutations(list(numbers))))))
    lst.extend([int(i) for i in list(numbers)])

    MAXIMUM = max(lst) + 1
    prime = []

    matrix = ( [False] * 2 ) + ( [True] * (MAXIMUM - 1) )

    for i in range(2, MAXIMUM):
        if matrix[i]:
            prime.append(i)

            for j in range(i*2, MAXIMUM, i):
                if j < MAXIMUM:
                    matrix[j] = False

    return len(list(set(lst) & set(prime)))

if __name__ == "__main__":
    print(solution("17"))   # 3
    print(solution("011"))  # 2
    print(solution("9999999"))  # 0