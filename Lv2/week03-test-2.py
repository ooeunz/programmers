# week03 모의고사-1
def turn_on_light(road, lights, d):
    for light in lights:
        low = light - d
        upper = light +d +1
        lst = [i for i in range(low, upper)]

        for i in range(len(lst)-1):
            road[(lst[i], lst[i+1])] = True
    
    if False not in road.values():
        return d
    else:
        return turn_on_light(road, lights, d+1)
    
def solution(road, lights):
    road = {(i, i+1):False for i in range(road)}
    return turn_on_light(road, lights, 1)

if __name__ == "__main__":
    print(solution(15, [15,5,3,7,9,14,0]))