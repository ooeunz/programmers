class Node():
    def __init__(self, num):
        self.empty = True
        self.nx_room = [num+1]


def solution(k: int, room_num: list):
    hotel = [Node(room) for room in range(k+2)]
    asign = []

    for room in room_num:
        if hotel[room].empty:
            asign.append(room)
            hotel[room].empty = False

            # TODO 다음 방이 비어있을 때 까지
            if hotel[hotel[room].nx_room[0]].empty:
                continue
            else:
                hotel[room].nx_room = hotel[hotel[room].nx_room[0]].nx_room

        else:   # 방이 비어있지 않다면
            while not hotel[room].empty:
                next_room = hotel[room].nx_room[0]
                hotel[room].nx_room = hotel[next_room].nx_room

                room = next_room

            hotel[room].empty = False
            asign.append(room)
    return asign


if __name__ == "__main__":
    print(solution(10, [1, 3, 4, 1, 3, 1]))  # [1,3,4,2,5,6]
