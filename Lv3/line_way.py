import math


def solution(n: int, k: int):
    people = [i for i in range(1, n+1)]

# 풀이: http://blog.naver.com/PostView.nhn?blogId=jwyoon25&logNo=221347789536&categoryNo=0&parentCategoryNo=0&viewDate=&currentPage=1&postListTopCurrentPage=1&from=postView&userTopListOpen=true&userTopListCount=5&userTopListManageOpen=false&userTopListCurrentPage=1
# 순열: https://shoark7.github.io/programming/algorithm/Permutations-and-Combinations
# 팩토리얼: https://shoark7.github.io/programming/algorithm/several-ways-to-solve-factorial-in-python


if __name__ == "__main__":
    print(solution(3, 5))
    print(solution(20, 20))
