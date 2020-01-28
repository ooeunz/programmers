# 주식 가격

def solution(prices):
    # initialization
    ans = []

    for i, price in enumerate(prices):
        if i == len(prices)-1:
            break

        cnt = 0
        for y in range(i+1, len(prices)):
            if price > prices[y]:
                cnt += 1
                break
            cnt += 1
        ans.append(cnt)
        
    ans.append(0)
    return ans

if __name__ == "__main__":
    print(solution([1, 2, 3, 2, 3]))    # [4, 3, 1, 1, 0]
    print(solution([2, 3, 4, 5, 6]))