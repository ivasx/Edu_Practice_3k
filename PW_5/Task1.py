nums_inp = []
for n in input('Введіть числа через пробіл: ').split():
    try:
        nums_inp.append(float(n))
    except ValueError:
        pass

positives = [n for n in nums_inp if n >= 0]
negatives = [n for n in nums_inp if n < 0]

min_index = nums_inp.index(min(nums_inp))
max_index = nums_inp.index(max(nums_inp))

s, e = sorted([max_index, min_index])
if e - s > 1:
    product = 1
    for i in nums_inp[s + 1 :e]:
        product *= i
else:
    product = 0

print(f'Масив: {nums_inp}')
print(f'Сума від\'ємних елементів масиву: {sum(negatives)}')
print(f'Добуток елементів масиву, розташованих між максимальним ({max(nums_inp)}) '
      f'і мінімальним ({min(nums_inp)}) елементами: {product}')