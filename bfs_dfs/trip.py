import copy


trip_book = []

def dfs(cur_pos: str, cur_tickets: list, path: str):
    for ticket in cur_tickets:
        str_pnt, end_pnt = ticket
        
        if cur_pos == str_pnt:
            next_tickets = copy.deepcopy(cur_tickets)
            next_tickets.remove(ticket)

            if not next_tickets:
                path.extend([str_pnt, end_pnt])
                trip_book.append(path)
                return

            next_path = copy.deepcopy(path)
            next_path.append(str_pnt)

            dfs(end_pnt, next_tickets, next_path)

def solution(tickets):
    dfs("ICN", tickets, [])
    
    return sorted(trip_book)[0]

if __name__ == "__main__":
    print(solution([["ICN", "JFK"], ["HND", "IAD"], ["JFK", "HND"]]))   # ["ICN", "JFK", "HND", "IAD"]
    print(solution([["ICN", "SFO"], ["ICN", "ATL"], ["SFO", "ATL"], ["ATL", "ICN"], ["ATL", "SFO"]]))   # ["ICN", "ATL", "ICN", "SFO", "ATL", "SFO"]