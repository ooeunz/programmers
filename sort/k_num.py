def solution(lst: list, commands: list):
    ans = []
    for command in commands:
        i, j, k = command

        ex_lst = lst[i-1 : j]
        ex_lst.sort()

        ans.append(ex_lst[k-1])
    return ans

if __name__ == "__main__":
    print(solution([1, 5, 2, 6, 3, 7, 4], [[2, 5, 3], [4, 4, 1], [1, 7, 3]]))

# 다른 사람 풀이
# def solution(lst: list, commands: list):
#     return list(map(lambda x: sorted(lst[x[0]-1 : x[1]])[x[2]-1], commands))
