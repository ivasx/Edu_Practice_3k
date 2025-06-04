import math

def f(x):
    return x - math.sin(x)

A = 0
B = math.pi / 2
M = 10

H = (B - A)/M

print(f'Обчислення функції x - sin(x) на відрізку AB, де A = {A}, B = {B}')
print(f"Відрізок: [{A}, {B}]\n")
print(f'{"i":<5} | {"Xi":<25} | {"Yi":<20}')
print('-' * 90)

for i in range(M + 1):
    Xi = A + i * H
    Yi = f(Xi)
    print(f'{i:<5} | Xi = {Xi:<20} | Yi = {Yi:<20}')