# initailzation
def legacy_network(apartment: list, w: int, stations: list):
    for station in stations:
        usage_network(apartment, w, station)

    # dubug
    # print("초기설정 아파트: {}".format(apartment))

# bound check함수
def bound_check(apartment: list, location):
    if location < 0 or location >= len(apartment):
        return False
    return True

# 통신이 사용가능함을 표시 함수
def usage_network(apartment: list, w: int, cur_loc: int):
    possible_network = w * w + 1

    start_loc = cur_loc - w
    end_loc = cur_loc + w + 1

    for idx in range(start_loc, end_loc):
        if bound_check(apartment, idx):
            apartment[idx] = 1

    # dubug
    # print("{}부터 {}까지 아파트에 통신을 사용가능하게 치크하였고,".format(start_loc, end_loc-1))
    # print("현재 아파트의 통신 사용 상태는: {}\n".format(apartment))
            
def solution(n: int, stations: list, w: int):
    # 아파트 개수+1 리스트 생성
    apartment = [0] * (n + 1)
    legacy_network(apartment, w, stations)

    non_network = 0
    ans = 0
    for idx in range(1, len(apartment)):
        if non_network == w or (non_network and apartment[idx]):
            usage_network(apartment, w, idx)
            non_network = 0
            ans += 1

            # debug
            # print("기지국 설치: {} 번째 아파트".format(idx))

        if apartment[idx] == 0:
            non_network += 1

    return ans

if __name__ == "__main__":
    print(solution(11, [4, 11], 1)) # 3
    print(solution(16, [9], 2)) # 3
