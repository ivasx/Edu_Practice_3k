def input_numbers_loop():
    sum_num = 0
    count = 0

    while True:
        try:
            num = int(input('Введіть число (0 для завершення): '))
        except ValueError:
            print('Введене вами значення не є числом.')
            continue

        if num == 0:
            break

        sum_num += num
        count += 1

    if count == 0:
        print('Ви не ввели жодного числа.')
    else:
        avg = sum_num / count
        print(f'Сума: {sum_num}')
        print(f'Кількість: {count}')
        print(f'Середнє арифметичне: {avg}')


if __name__ == '__main__':
    input_numbers_loop()
