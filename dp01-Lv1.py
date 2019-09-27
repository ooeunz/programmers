# 완주하지 못한 선수
from collections import Counter
def solution(participant, completion):
    participant = Counter(participant)
    completion = Counter(completion)

    return list(participant - completion).pop()

if __name__ == "__main__":
    print(solution(["leo", "kiki", "eden"], ["eden", "kiki"]))
    print(solution(["marina", "josipa", "nikola", "vinko", "filipa"], ["josipa", "filipa", "marina", "nikola"]))
    print(solution(["mislav", "stanko", "mislav", "ana"], ["stanko", "ana", "mislav"]))


# set 자료형으로 풀었다가 중복된 선수들을 걸러내지 못하여서 Counter함수로 풀었음.