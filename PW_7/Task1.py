import random

A = []
rows = cols = 5

for i in range(rows):
    row = []
    for j in range(cols):
        row.append(random.randint(0, 9))  # a_ij > 0
    A.append(row)

print('Матриця A:')
for row in A:
    for x in row:
        print(f'{x:2}', end=' ')
    print()
print()

for i in range(rows):
    A[i][0], A[i][cols-1] = A[i][cols-1], A[i][0]

print('Матриця A:')
for row in A:
    for x in row:
        print(f'{x:2}', end=' ')
    print()
print()