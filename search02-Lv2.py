# 카펫
# row >= col
def solution(brown, red):
    pair = []
    for i in range(1, int(red**0.5) +1):
        if red % i == 0:
            pair.append([i, red//i])
    for row, col in pair:
        if (row * 2) + (col * 2) + 4 == brown:
            return [col+2, row+2]

if __name__ == "__main__":
    print(solution(10, 2))  # [4, 3]
    print(solution(8, 1))   # [3, 3]
    print(solution(24, 24)) # [8, 6]
    print(solution(12, 4))  # [4, 4]
    print(solution(13, 3))  # [4, 4] -> red가 홀수일 때