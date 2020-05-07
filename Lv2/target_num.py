cnt = 0

def dfs(node: int, cur_value: int, numbers: list, target: int):
    if node == len(numbers):
        if cur_value == target:
            global cnt
            cnt += 1
        return
    
    dfs(node + 1, cur_value + numbers[node], numbers, target)
    dfs(node + 1, cur_value - numbers[node], numbers, target)

def solution(numbers: int, target: int):
    dfs(0, 0, numbers, target)
    return cnt

if __name__ == "__main__":
    print(solution([1, 1, 1, 1, 1], 3)) # 5