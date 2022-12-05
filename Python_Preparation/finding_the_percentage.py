if __name__ == '__main__':
    n = int(input())
    student_marks = {}
    for _ in range(n):
        name, *line = input().split()
        scores = list(map(float, line))
        student_marks[name] = scores
    query_name = input()

    mrks = student_marks[query_name]
    total_mrk = 0
    for i in mrks:
        total_mrk += i
    av = round(float(total_mrk/len(mrks)), 2)
    print(f'{av:.2f}')