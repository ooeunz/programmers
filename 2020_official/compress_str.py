def compress(ss: str, num: int):
    ans = ''
    cnt = 1

    for i in range(num, len(ss), num):
        std = ss[i-num:i]

        if std == ss[i:i+num]:
            cnt += 1
        else:
            if cnt == 1:
                ans += std
            else:
                ans += str(cnt) + std
                cnt = 1

    if len(ss[i:num+i]) == num:
        if cnt == 1:
            ans += std
        else:
            ans += str(cnt) + std
    else:
        ans += ss[i:num+i]

    # print(ans)
    return len(ans)


def solution(ss: str):
    if len(ss) == 1:
        return 1

    ans = float('inf')
    for i in range(1, len(ss)):
        ans = min(ans, compress(ss, i))

    return ans


if __name__ == "__main__":
    print(solution("aabbaccc"))  # 7
    print(solution("ababcdcdababcdcd"))  # 9
    print(solution("abcabcdede"))   # 8
    print(solution("abcabcabcabcdededededede"))  # 14
    print(solution("xababcdcdababcdcd"))    # 17
