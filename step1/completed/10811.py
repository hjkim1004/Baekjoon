def reverse(arr: list, s: int, e: int) -> list:
    return arr[:s] + arr[s:e+1][::-1] + arr[e+1:]


if __name__ == '__main__':
    N, M = [int(e) for e in input().split()]
    result = [str(i + 1) for i in range(N)]

    for i in range(M):
        s, e = [int(e) for e in input().split()]
        result = reverse(result, s-1, e-1)

    print(' '.join(result))
