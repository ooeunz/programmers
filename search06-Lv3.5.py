# N-Queen

def is_promising(queen, node, n):
    y, x = node
    # row
    if y in queen.keys() or x in queen.values():
        return False
    # diagonal
        m = y+n
        [ for i, j range(m)]

def dfs(graph, chess_board):
    visit = set()
    stack = []

    stack.append(graph[(0, 0)])

    while stack:
        node = stack.pop()
        if node not in visit:
            visit.add(node)
            stack.extend(graph[node])



def solution(n):
    chess_board = [[False for x in range(n)] for y in range(n)]
    graph = {}
    for x in range(n-1):
        for y in range(n-1):
            if y == 0:
                graph[(y, x)] = [(y+1,x), (y, x+1)]
            else:
                graph[(y, x)] = [(y+1, x)]
    print(graph)