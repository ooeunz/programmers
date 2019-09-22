# week02 모의고사-2 
def solution(brackets):
    stack = []
    package = {
        '(' : ')',  # small
        '{' : '}',  # middle
        '[' : ']'   # big
    }

    for braket in brackets:
        if not stack:
            stack.append(braket)
        elif braket in package.keys():
            stack.append(braket)
        elif package[stack[-1]] == braket:
            stack.pop()
        
    return False if stack else True

if __name__ == "__main__":
    print(solution("{{}}"))
    print(solution("({})[]"))
