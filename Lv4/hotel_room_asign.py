class Node():
    def __init__(self, num):
        self.empty = True
        self.next_room = num


def solution(k, room_number):
    hotel = [Node(x) for x in range(k)]
    result = []

    for room in room_number:
        if hotel[room].empty:
            result.append(room)
            hotel[room].empty = False
            hotel[room].next_room = room + 1
        else:
            visited = [room]
            next_visit = hotel[room].next_room

            while True:
                if hotel[next_visit].empty:
                    result.append(next_visit)

                    hotel[next_visit].empty = False
                    hotel[next_visit].next_room = next_visit + 1

                    for v in visited:
                        hotel[v].next_room = next_visit + 1
                    break
                else:
                    next_visit = hotel[next_visit].next_room
                    visited.append(next_visit)

    return result


if __name__ == "__main__":
    print(solution(10, [1, 3, 4, 1, 3, 1]))  # [1,3,4,2,5,6]
