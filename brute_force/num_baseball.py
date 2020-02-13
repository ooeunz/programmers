from itertools import permutations

def judgment_ball(qst_num: str, ans_num: str):
    ball = 0
    for qst in qst_num:
        if qst in ans_num:
            ball += 1

    return ball - judgment_strike(qst_num, ans_num)

def judgment_strike(qst_num: str, ans_num: str):
    strike = 0
    for qst, ans in zip(qst_num, ans_num):
        if qst == ans:
            strike += 1

    return strike

def solution(baseball: list):
    number_of_case =  set(''.join(idx) for idx in permutations("123456789", 3))
    
    for rounds in baseball:
        qst_num, strike, ball = rounds
        qst_num = str(qst_num)
        difference = set()

        for ans_num in number_of_case:
            if strike == judgment_strike(qst_num, ans_num) and ball == judgment_ball(qst_num, ans_num):
                difference.add(ans_num)
                
        if difference:
            number_of_case = number_of_case & difference

    return len(number_of_case)

if __name__ == "__main__":
    print(solution([[123, 1, 1], [356, 1, 0], [327, 2, 0], [489, 0, 1]]))

