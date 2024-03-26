if __name__ == '__main__':
    cnt = 0
    while cnt < 100:
        cnt += 1
        try:
            msg = input()
            print(msg)
        except EOFError:
            break
