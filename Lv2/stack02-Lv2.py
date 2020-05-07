# 짝지어 제거하기
def solution(str):
    stack = []

    for s in str:
        if not stack:
            stack.append(s)
            continue
        if s == stack[-1]:
            stack.pop()
        else:
            stack.append(s)
    return 0 if stack else 1

if __name__ == "__main__":
    print(solution("baabaa"))