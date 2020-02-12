import heapq


def solution(operations):
    min_heap = []
    max_heap = []

    for operation in operations:
        oper, num = operation.split()
        num = int(num)
        
        if oper == "I":
            heapq.heappush(min_heap, num)
            heapq.heappush(max_heap, -num)
        elif oper == "D" and min_heap:
            if num > 0:
                min_heap.remove(-heapq.heappop(max_heap))
            else:
                max_heap.remove(-heapq.heappop(min_heap))
        
    return [max(min_heap), heapq.heappop(min_heap)] if min_heap else [0, 0]

if __name__ == "__main__":
    print(solution(["I 16","D 1"]))
    print(solution(["I 7","I 5","I -5","D -1"]))