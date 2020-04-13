def compress(ss: str, num: int):
    ans = ''

    for i in range(num, len(ss), num):
        std = ss[i-num:i]
        cnt = 1

        if std == ss[i:i+num]:
            cnt += 1
        else:
            if cnt > 1:
                ans += str(cnt) + std
                cnt = 1
            else:
                ans += std

    if len(ss[i:num+i]) == num:
        if cnt > 1:
            ans += str(cnt) + std
        else:
            ans += std
    else:
        ans += ss[i:num+i]

    print(ans)
    return len(ans)


def solution(ss: str):
    if len(ss) == 1:
        return 1

    ans = float('inf')
    for i in range(1, len(ss) // 2):
        ans = min(ans, compress(ss, i))

    return ans

# def solution(s):
#     answers = []
#     if len(s) == 1:
#         return 1
#     for i in range(1, len(s)):
#         answer = ''
#         count = 1
#         for j in range(i, len(s), i):
#             if s[j-i:j] == s[j:j+i]:
#                 count += 1
#             else:
#                 if count == 1:
#                     answer += s[j-i:j]
#                 else:
#                     answer += str(count)+s[j-i:j]
#                     count = 1
#         if len(s[j:j+i]) == i:
#             if count == 1:
#                 answer += s[j-i:j]
#             else:
#                 answer += str(count)+s[j-i:j]
#                 count = 1
#         else:
#             answer += s[j:j+i]
#         answers.append(len(answer))
#     return min(answers)


if __name__ == "__main__":
    print(solution("aabbaccc"))
    # print(solution("ababcdcdababcdcd"))
