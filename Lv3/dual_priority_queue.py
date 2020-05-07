import heapq


def solution(operations):
    heap = []

    for operation in operations:
        oper, num = operation.split()
        num = int(num)
        
        if oper == "I":
            heapq.heappush(heap, num)
        elif heap:
            if num > 0:
                heap.remove(max(heap))
            else:
                heapq.heappop(heap)
        
    return [max(heap), heapq.heappop(heap)] if heap else [0, 0]

if __name__ == "__main__":
    print(solution(["I 16","D 1"]))
    print(solution(["I 7","I 5","I -5","D -1"]))