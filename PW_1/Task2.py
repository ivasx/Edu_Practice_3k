while True:
    try:
        num1, num2 = input('Введіть два числа (через пробіл): ').split()
        num1 = float(num1)
        num2 = float(num2)
        break
    except ValueError:
        print('Введені вами значення некоректні.')

print(f'Сума: {num1 + num2:.2f}')
print(f'Добуток: {num1 * num2:.2f}')