from collections import deque

def solution(n, computers):
    n = [i for i in range(n)]
    visited = set()
    network = []
    ans = []

    queue = deque()
    # 아직 방문하지 않은 컴퓨터가 있다면
    while len(visited) != len(n):
        start = list(set(n) - set(visited))[0]
        visited.add(start)
        network.append(start)

        queue.append(start)
        while queue:
            cur_node = queue.popleft()
            for search_node in range(len(computers[cur_node])):
                if computers[cur_node][search_node] and search_node not in visited:
                    visited.add(search_node)
                    network.append(search_node)
                    queue.append(search_node)
        ans.append(network)
        network = []
    return len(ans)
        

if __name__ == "__main__":
    print(solution(3, [[1, 1, 0], [1, 1, 0], [0, 0, 1]]))   # 2
    print(solution(3, [[1, 1, 0], [1, 1, 1], [0, 1, 1]]))   # 1