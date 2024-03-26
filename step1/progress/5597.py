# 제목: 과제 안내신 분..?
# 링크: https://www.acmicpc.net/problem/5597

if __name__ == '__main__':
    students = set([input() for e in range(28)])
    total = set([str(i+1) for i in range(30)])

    print(f"total: {len(total)}, {total}\nstudents: {len(students)}, {students}")
    print('\n'.join(sorted(total.difference(students))))