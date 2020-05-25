dp = dict()

def dfs(height: int, width: int, past_dp: str, land: list):
    if height == len(land):
        return dp[past_dp]

    cur_dp = past_dp + str(width)

    if cur_dp not in dp:
        dp[cur_dp] = dp[past_dp] + land[height][width]

    return max([dfs(height+1, i, cur_dp, land) for i in range(4) if i != width])

def solution(land: list):
    ans = float('-inf')

    for i in range(4):
        dp[str(i)] = land[0][i]
        for j in range(4):
            if i != j:
                ans = max(ans, dfs(1, j, str(i), land))
    return ans
    
if __name__ == "__main__":
    print(solution([[1,2,3,5],[5,6,7,8],[4,3,2,1]]))