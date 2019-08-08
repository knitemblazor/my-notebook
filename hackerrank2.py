




if __name__ == '__main__':
    n = int(input())
    student_marks = {}
    if (2<=n<=10):
        for _ in range(n):
            name, *line = input().split()
            scores = list(map(float, line))
            student_marks[name] = scores
    query_name = input()
    inter = sum(student_marks[query_name])/len(scores)
    print("{:.2f}".format(inter))

