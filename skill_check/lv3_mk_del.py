from collections import defaultdict
import copy


visited = set()

def dfs(cur_node: str, maps: dict, dist: int, K: int, past_node: tuple):
    if dist > K:
        return
    if cur_node not in visited and dist <= K:
        visited.add(cur_node)

    for des, time in maps[cur_node]:
        if past_node:
            past_cur, past_des = past_node
            if (cur_node, des) == (past_cur, past_des) or (cur_node, des) == (past_des, past_cur):
                continue
        dfs(des, maps, dist + time, K, (cur_node, des))

def solution(N, road, K):
    maps = defaultdict(list)

    for r in road:
        maps[r[0]].append([r[1], r[2]])
        maps[r[1]].append([r[0], r[2]])

    dfs(1, maps, 0, K, tuple())
    return len(visited)

if __name__ == "__main__":
    print(solution(5, [[1,2,1],[2,3,3],[5,2,2],[1,4,2],[5,3,1],[5,4,2]], 3))    # 4
    # print(solution(6, [[1,2,1],[1,3,2],[2,3,2],[3,4,3],[3,5,2],[3,5,3],[5,6,1]], 4))    # 4
