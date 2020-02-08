from collections import Counter


def set_total_listen(genres: list):
    total_listen = {}

    for genre in list(set(genres)):
        total_listen[genre] = 0
    
    return total_listen

def extract_key(dic: dict):
    result = sorted(dic.items(), key=lambda x: x[1], reverse=True)
    
    return list(map(lambda x: x[0], result))

def sort_genres(listen: dict, genres: list, plays: list):
    for idx, genre in enumerate(genres):
        listen[genre] += plays[idx]

    return extract_key(listen)

def collect_genre(target: str, genres: list, plays: list):
    collect = {}

    for idx, genre in enumerate(genres):
        if target == genre:
            collect[idx] = plays[idx]

    result = extract_key(collect)

    return result[:2]


def solution(genres: list, plays: list):
    listen = sort_genres(set_total_listen(genres), genres, plays)
    
    ans = []
    for li in listen:
        ans.extend(collect_genre(li, genres, plays))
    return ans
    


if __name__ == "__main__":
    print(solution(["classic", "pop", "classic", "classic", "pop"], [500, 600, 150, 800, 2500]))