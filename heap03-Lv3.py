import heapq

healths = [300, 200, 500]
items = [[1000, 600], [400, 500], [300, 100]]
def solution(healths, items):    
    healths.sort()
    for i in range(len(items)):
        items[i][0] = -items[i][0]
    heapq.heapify(items)
    
    for j in range(len(items)):
        check = float('inf')
        remember = 0
        for i in range(len(healths)):
            if healths[i] - items[j][1] <= check and healths[i] - items[j][1] >= 100:
                check = healths[i] - items[j][1]
                remember = i+1
        if remember:
            items[j][0] = abs(items[j][0])
            del healths[remember-1]
    ans = []
    for i in range(len(items)):
        if items[i][0] >=0:
            ans.append(i+1)
    return ans

if __name__ == "__main__":
    print(solution(healths, items))
