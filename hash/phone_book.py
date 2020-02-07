def solution(phone_book):
    phone_book.sort()

    for idx in range(len(phone_book)-1):
        for i, value in enumerate(phone_book[idx]):
            value != phone_book[idx+1][i]
            

    return phone_book

if __name__ == "__main__":
    print(solution(["119", "97674223", "1195524421"]))  # false