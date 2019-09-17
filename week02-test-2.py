# week02 모의고사-2 
def solution(s):
    stack = []
    SMALL, MIDDLE, BIG = '(', '{', '['
    CLOSE_SMALL, CLOSE_MIDDLE, CLOSE_BIG = ')', '}', ']'
    s = s.replace("[]", "")
    s = s.replace("{}", "")
    s = s.replace("()", "")
    for i in s:
        if not stack:
            stack.append(i)
            continue
        if i == SMALL:
            stack.append(i)
        elif i == MIDDLE:
            stack.append(i)
        elif i == BIG:
            stack.append(i)
        
        if i == CLOSE_SMALL and stack[-1] == SMALL:
            stack.pop()
        elif i == CLOSE_MIDDLE and stack[-1] == MIDDLE:
            stack.pop()
        elif i == CLOSE_BIG and stack[-1] == BIG:
            stack.pop()
        
    return False if stack else True

if __name__ == "__main__":
    print(solution("{{}}"))
    print(solution("({})[]"))
