def solution(arrng):
    beam = 0
    answer = 0

    OPEN, CLOSE, LASER = '(', ')', 'l'

    arrng = arrng.replace('()', LASER)

    for a in arrng:
        if a == OPEN:
            beam += 1
        elif a == CLOSE:
            beam -= 1
            answer += 1
        elif a == LASER:
            answer += beam

    return answer

print(solution("()(((()())(())()))(())"))