def solution(iron_bar):
    OPEN = "("
    CLOSE = ")"

    iron_bar = iron_bar.replace("()", "L")
    stack = []
    cnt = 0

    for iron in iron_bar:
        if iron == "L":
            cnt += len(stack)
        elif iron == OPEN:
            stack.append(OPEN)
        elif iron == CLOSE:
            stack.pop()
            cnt += 1
    return cnt

if __name__ == "__main__":
    print(solution("()(((()())(())()))(())"))   # 17