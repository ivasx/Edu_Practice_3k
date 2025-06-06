A0 = 2
A = [A0]

for n in range(4):
    A_n = A[n]
    A_next = A_n**2 / 2 + A_n / 3
    A.append(A_next)

print('Перші 5 елементів ряду:', end=' ')
for x in A:
    print(round(x, 2), end=' ')
print("\nСума перших 5 елементів ряду:", sum(A))
