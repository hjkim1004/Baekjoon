if __name__ == '__main__':
    origin = [1, 1, 2, 2, 2, 8]
    after = [str(origin[i] - int(e)) for i, e in enumerate(input().split())]
    print(' '.join(after))
