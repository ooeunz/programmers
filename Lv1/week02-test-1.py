# week02 모의고사-1
def solution(seats):
    space = {}
    ans = 0
    for seat in seats:
        x, y = seat
        if (x, y) in space:
            continue
        else:
            space[(x, y)] = True
            ans += 1
    return ans

if __name__ == "__main__":
    print(solution([[1,1],[2,2],[3,3]]))
    print(solution([[1,1],[2,1],[1,2],[3,4],[2,1],[2,1]]))