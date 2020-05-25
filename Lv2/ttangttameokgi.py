def solution(land: list):
    ans = 0
    memory = 4
    for l in land:
        memory, v = max([(i, v) for i, v in enumerate(l) if i != memory], key=lambda x: x[1])
        ans += v
    return ans

if __name__ == "__main__":
    print(solution([[1,2,3,5],[5,6,7,8],[4,3,2,1]]))