import math

def solution(brown, red):
    total_carpet = brown + red

    for i in range(3, int(total_carpet ** 0.5) + 1):
        if total_carpet % i == 0:
            height = i
            width = total_carpet // i
            if (width - 2) * (height - 2) == red:
                return [max(height, width), min(height, width)]

if __name__ == "__main__":
    print(solution(10, 2))
    print(solution(8, 1))
    print(solution(24, 24))
