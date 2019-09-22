from itertools import product
# 주사위 게임
def solution(monsters, S1, S2, S3):
    # initialization
    max_dice = S1 + S2 + S3 + 1
    field = [True] * (max_dice + 99)
    count = 0
    for monster in monsters:
        field[monster] = False

    S1 = [i for i in range(1, S1+1)]
    S2 = [i for i in range(1, S2+1)]
    S3 = [i for i in range(1, S3+1)]

    dice_case = list(map(sum, list(product(S1, S2, S3))))

    for dice in dice_case:
        if field[dice+1] == True:
            count += 1
    
    return int(count / len(dice_case) * 1000)

if __name__ == "__main__":
    print(solution([4, 9, 5, 8], 2, 3, 4))
    print(solution([4, 9, 5, 8], 2, 3, 3))