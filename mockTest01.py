m = 2
n = 4
infests = [[1,4],[2,2]]
vaccinateds = [[1,2]]

def infect(x, y, infects, vaccinateds, office, ans):
    if office[x][y] == vaccinateds:    # 백신 접종자라면
        return
    elif office[x][y] == infects:    # 감염자라면
        return
    else:
        office[x][y] = True
        ans += 1
        return ans
    infect(x+1, y, infects, vaccinateds, office, ans)
    infect(x-1, y, infects, vaccinateds, office, ans)
    infect(x, y+1, infects, vaccinateds, office, ans)
    infect(x, y-1, infects, vaccinateds, office, ans)


def solution(m, n, infects, vaccinateds):
    # make office
    ans = 0
    office = []
    inject = []
    for i in range(m):
        for j in range(n):
            inject.append(False)
        office.append(list(inject))
        inject.clear()
    infects = [-1 for infect in infects]
    
    
    answer = infect(0, 0, infects, vaccinateds, office, ans)
    return answer


if __name__ == "__main__":
    solution(m, n, infests, vaccinateds)