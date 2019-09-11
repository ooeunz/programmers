# 게임 아이템
import heapq

healths = [200,120,150]	
items = [[30,100],[500,30],[100,400]]

def solution(healths, items):    
    healths.sort()
    for item in items:
        item[0] = -item[0]
    heapq.heapify(items)
    
    for item in items:
        check = float('inf')
        remember = 0
        for health in healths:
            if health - item[1] <= check and health - item[1] >= 100:
                check = health - item[1]
                remember = health
            if remember:
                item[0] = abs(item[0])
                healths.remove(remember)
                remember = 0
    ans = []
    for i in range(len(items)):
        if items[i][0] >= 0:
            ans.append(i+1)
    return ans

if __name__ == "__main__":
    print(solution(healths, items))
