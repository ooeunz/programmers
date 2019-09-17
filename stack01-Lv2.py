# 쇠막대기
def solution(irons):
    # initialization
    irons = irons.replace("()", "l")

    ans = 0
    stack = []

    for iron in irons:
        if iron == "(":
            stack.append(iron)
        elif iron == ")":
            stack.pop()
            ans += 1
        elif iron == "l":
            ans += len(stack)
    return ans
    
if __name__ == "__main__":
    print(solution("()(((()())(())()))(())"))