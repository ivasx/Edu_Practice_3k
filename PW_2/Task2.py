def input_numbers(sum_num = 0, count = 0):
    num = input('Введіть число (0 для завершення): ')
    try:
        num = int(num)
    except ValueError:
        return input_numbers(sum_num, count)

    if num == 0:
        if count == 0:
            print('Ви не ввели жодного числа.')
            return None

        avg = sum_num / count
        print(f'Сума: {sum_num}')
        print(f'Кількість: {count}')
        print(f'Середнє арифметичне: {avg}')
        return None
    else:
        return input_numbers(sum_num + num, count + 1)

if __name__ == '__main__':
    input_numbers()
