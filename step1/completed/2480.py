def play_game(arr: list):
    arr_hash = {}
    for e in arr:
        e = int(e)
        if e not in arr_hash:
            arr_hash[e] = 1
        else:
            arr_hash[e] += 1

    keys = list(arr_hash.keys())
    entries = arr_hash.items()

    if len(keys) == 3:
        return max(keys) * 100
    elif len(keys) == 2:
        cnt = (list(map(lambda x: x[0], filter(lambda x: x[1] == 2, entries)))[0])
        return 1000 + 100 * cnt
    elif len(keys) == 1:
        return 10000 + 1000 * keys[0]


if __name__ == '__main__':
    print(play_game(input().split()))
