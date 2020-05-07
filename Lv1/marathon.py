# 마라톤
import collections

def solution(participant, completion):
    ans = collections.Counter(participant) - collections.Counter(completion)
    return list(ans.keys())[0]
    
if __name__ == "__main__":
    print(solution(["leo", "kiki", "eden"], ["eden", "kiki"]))