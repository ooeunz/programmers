# N-Queen
def solution(n):
    visit = []
    stack = []
    start_node = (0, 0)
    graph = []

    stack.append(start_node)

    while stack:
        node = stack.pop()
        if node not in visit:   # 방문하지 않았다면
            visit.append(node)
            stack.extend(graph[node])