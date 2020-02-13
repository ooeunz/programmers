def solution(n: int, lost: list, spare: list):
    clothes = [1 for _ in range(n+1)]

    self_lost = set(set(lost) & set(spare))
    lost = list(set(lost) - self_lost)
    spare = list(set(spare) - self_lost)

    for l in lost:
        clothes[l] -= 1
    for s in spare:
        clothes[s] += 1

    for lost_person in lost:
        if clothes[lost_person-1] == 2:
            clothes[lost_person-1] -= 1
            clothes[lost_person] += 1

        elif lost_person+1 < len(clothes) and clothes[lost_person+1] == 2:
            clothes[lost_person+1] -= 1
            clothes[lost_person] += 1

    return len(list(filter(lambda x: x > 0, clothes))) - 1

if __name__ == "__main__":
    print(solution(5, [2, 4], [1, 3, 5]))   # 5
    print(solution(5, [2, 4], [3]))   # 4
    print(solution(3, [3], [1]))   # 2
    print(solution(8, [1, 3, 5], [4, 5])) # 7

