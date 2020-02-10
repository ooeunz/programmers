def solution(paper):
    paper.sort()
    l = len(paper)
    
    for i in range(l):
        if paper[i] >= l-i:
            return l-i 
    return 0

if __name__ == "__main__":
    print(solution([3, 0, 6, 1, 5]))    # 3
    print(solution([10000, 10000, 10000, 10000, 10000]))
    print(solution([22, 42]))
