# 타겟 넘버
cnt = 0

def dfs(node: int, numbers: list, target: int, cur_value: int):
    if node == len(numbers):
        if cur_value == target:
            global cnt
            cnt += 1
        return
    
    dfs(node + 1, numbers, target, cur_value + numbers[node])
    dfs(node + 1, numbers, target, cur_value - numbers[node])

def solution(numbers, target):
    dfs(0, numbers, target, 0)
    global cnt
    return cnt

if __name__ == "__main__":
    print(solution([1, 1, 1, 1, 1], 3)) # 5