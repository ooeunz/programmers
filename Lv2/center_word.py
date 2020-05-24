def solution(s: str):
    return s[len(s) // 2] if len(s) % 2 else s[len(s)//2-1:len(s)//2+1]
    
if __name__ == "__main__":
    print(solution("abcde"))
    print(solution("qwer"))