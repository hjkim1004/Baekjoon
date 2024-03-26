def check_palindrome(param: str) -> bool:
    length = len(param)
    c = length // 2
    return param[:c] == param[c:][::-1] if length % 2 == 0 else param[:c] == param[c + 1:][::-1]


if __name__ == '__main__':
    letter = input()
    print(int(check_palindrome(letter)))
