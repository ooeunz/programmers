# week02 모의고사-1
def solution(seats):
    ans = set([tuple(seat) for seat in seats])
    return len(ans)

if __name__ == "__main__":
    print(solution([[1,1],[2,2],[3,3]]))
    print(solution([[1,1],[2,1],[1,2],[3,4],[2,1],[2,1]]))