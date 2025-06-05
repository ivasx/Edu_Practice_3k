import math
import numpy
from tabulate import tabulate

a = -5
b = 2
t_val = numpy.arange(0, 3, 0.15)
results = []

for t in t_val:
    if t < 1:
        y = 1
    elif 1 <= t <= 2:
        y = a * t * math.log(t)
    elif t > 2:
        y = math.exp(a * t) * math.cos(b * t)

    results.append((t, y))

print('-' * 30)
print(f'|{"№":<3}|{"t":>6} | {"y":>15}|')
print('-' * 30)
for i, (t, y) in enumerate(results):
    print(f'|{i:<3}|{t:6.2f} | {y:15.6f}|')
print('-' * 30)