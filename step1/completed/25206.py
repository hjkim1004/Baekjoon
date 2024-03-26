if __name__ == '__main__':
    rank_hash = {'A+': 4.5, 'A0': 4.0, 'B+': 3.5, 'B0': 3.0, 'C+': 2.5, 'C0': 2.0, 'D+': 1.5, 'D0': 1.0, 'F': 0.0}

    cnt_val = 0
    sum_val = 0
    for i in range(20):
        name, credit, rank = input().split()

        if rank == 'P':
            continue

        credit = int(credit.replace('.0', ''))
        cnt_val += credit
        sum_val += rank_hash[rank] * credit

    print(sum_val / cnt_val)