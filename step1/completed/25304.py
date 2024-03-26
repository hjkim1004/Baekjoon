if __name__ == '__main__':
    total = int(input())
    calc = 0
    for e in range(int(input())):
        price, cnt = input().split()
        calc += int(price) * int(cnt)

    print("Yes" if total == calc else "No")