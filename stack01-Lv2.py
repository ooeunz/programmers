# 쇠막대기
def solution(irons):
    # initialization
    OPEN, CLOSE, LASER = '(', ')', 'l'
    irons = irons.replace("()", LASER)

    ans = 0
    stack = []

    # running
    for iron in irons:
        if iron == OPEN:
            stack.append(OPEN)
        elif iron == CLOSE:
            stack.pop()
            ans += 1
        elif iron == LASER:
            ans += len(stack)
    return ans
    
if __name__ == "__main__":
    print(solution("()(((()())(())()))(())"))