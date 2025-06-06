import random

A = []
rows, cols = 10, 15
for i in range(rows):
    row = []
    for j in range(cols):
        row.append(random.randint(0, 100))  # a_ij > 0
    A.append(row)

print('Матриця A:')
for row in A:
    for x in row:
        print(f'{x:3}', end=' ')
    print()
print()

sums = []
positives = []

for col in zip(*A):
    sums.append(sum(x for x in col if x > 0))
    positives.append(sum(1 for x in col if x >0))
print('—' * 100)
print('Сума додатніх елементів по стовпцях:', *sums)
print('—' * 100)
print('Кількість додатніх елементів по стовпцях:', *positives)
print('—' * 100)

