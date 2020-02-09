from collections import deque

def compare(a_word, b_word):
    cnt = 0
    for a, b in zip(a_word, b_word):
        if a != b:
            cnt += 1
    if cnt == 1:
        return True
    return False

def solution(begin, target, words):
    if target not in words:
        return 0

    visited = {begin}
    queue = deque([(begin, 0)])

    while queue:
        node, dist = queue.popleft()
        if node == target:
            return dist
            
        for word in words:
            if word not in visited and compare(node, word):
                visited.add(word)
                queue.append((word, dist+1))
    return 0

if __name__ == "__main__":
    print(solution("hit", "cog", ["hot", "dot", "dog", "lot", "log", "cog"]))
    print(solution("hit", "cog", ["hot", "dot", "dog", "lot", "log"]))