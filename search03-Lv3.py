from itertools import product
# 주사위 게임
def solution(monster, S1, S2, S3):
    # initialization
    max_dice = S1 + S2 + S3 + 1
    field = [True] * (max_dice + 2)
    count = 0
    for i in monster:
        field[i] = False

    S1 = [i for i in range(1, S1+1)]
    S2 = [i for i in range(1, S2+1)]
    S3 = [i for i in range(1, S3+1)]

    dice_case = list(map(sum, list(product(S1, S2, S3))))
    
    for dice in dice_case:
        if field[dice] == True:
            count += 1
    
    return count / len(dice_case)






if __name__ == "__main__":
    # print(solution([4, 9, 5, 8], 2, 3, 4))
    print(solution([4, 9, 5, 8], 2, 3, 3))