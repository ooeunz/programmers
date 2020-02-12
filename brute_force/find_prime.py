from itertools import permutations

def solution(numbers):
    lst = list(set(map(int, [''.join(j) for i in range(1, len(numbers)+1) for j in permutations(numbers, i)])))
    MAXIMUM = max(lst)
    prime = []

    matrix = ( [False] * 2 ) + ( [True] * (MAXIMUM - 1) )

    for i in range(2, MAXIMUM+1):
        if matrix[i]:
            prime.append(i)

            for j in range(i*2, MAXIMUM+1, i):
                if matrix[j]:
                    matrix[j] = False

    return len(list(set(lst) & set(prime)))

if __name__ == "__main__":
    print(solution("17"))   # 3
    print(solution("011"))  # 2
    print(solution("9999999"))  # 0