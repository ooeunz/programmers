# 운송 트럭
def solution(max_weight, specs, names):
    ans = 1
    specs = dict(specs)
    truck = max_weight
    
    for i in specs:
        specs[i] = int(specs[i])
    
    while names:
        order = names.pop()

        if truck - specs[order] >= 0:
            truck -= specs[order]
        else:
            truck = max_weight
            truck -= specs[order]
            ans += 1
    return ans

if __name__ == "__main__":
    print(solution(300, [["toy","70"], ["snack", "200"]], ["toy", "snack", "snack"]))
    print(solution(200, [["toy","70"], ["snack", "200"]], ["toy", "snack", "toy"]))