def solution(s):
    lst = list(map(int, s.split(' ')))
    return "{} {}".format(str(min(lst)), str(max(lst)))

if __name__ == "__main__":
    print(solution("1 2 3 4"))
    print(solution("-1 -2 -3 -4"))
