if __name__ == '__main__':
    import math as m
    n = int(input())
    avg=0.0
    student_marks = {}
    for _ in range(n):
        name, *line = input().split()
        scores = list(map(float, line))
        student_marks[name] = scores
    query_name = input()
    if query_name in student_marks:
        x = ((float(student_marks[query_name][0]) + float(student_marks[query_name][1]) + float(student_marks[query_name][2])) / 3)
    
    print('%.2f' % x)
