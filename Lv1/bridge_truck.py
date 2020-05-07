# 다리를 지나는 트럭
import sys
import copy
from collections import deque

def solution(bridge_length: int, weight: int, truck_weights: list):
    
    # initialization
    trucks = deque(truck_weights)
    weight -= trucks[0]

    bridge = deque([trucks.popleft()])
    time_table = [0]

    cur_time = 1
    while bridge:
        time_table = list(map(lambda x: x+1, time_table))
        ex_time_table = copy.deepcopy(time_table)
        cur_time += 1

        for time in time_table:
            if time == bridge_length:
                del ex_time_table[0]
                weight += bridge.popleft()
        time_table = ex_time_table

        if trucks and weight >= trucks[0]:
            weight -= trucks[0]
            bridge.append(trucks.popleft())
            time_table.append(0)

        # print("경과시간: {}".format(cur_time))
        # print("다리 위 트럭: {}\n".format(bridge))
        
    return cur_time

if __name__ == "__main__":
    print(solution(2, 10, [7, 4, 5, 6]))    # 8
    print(solution(100, 100, [10])) # 101
    print(solution(100, 100, [10, 10, 10, 10, 10, 10, 10, 10, 10, 10])) # 110