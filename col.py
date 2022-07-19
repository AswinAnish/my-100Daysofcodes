num_students = int(input())
relevant_pos = None
total = 0
for num in range(num_students + 1):
    if num == 0:
        titles = list(filter(lambda el: el != '', input().split(' ')))
        relevant_pos = titles.index('MARKS')
        continue
    total += int(list(filter(lambda el: el != '', input().split(' ')))[relevant_pos])

print(round(float(total) / num_students, 2))
