if __name__ == '__main__':
    letter = input()
    crotia = [('c=', 'č'), ('c-', 'ć'), ('dz=', '3'), ('d-', 'đ'), ('lj', '1'), ('nj', '2'), ('s=', 'š'), ('z=', 'ž')]
    for e in crotia:
        before, after = e
        letter = letter.replace(before, after)

    print(len(letter))
