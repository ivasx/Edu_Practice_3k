def get_numbers(number_of_numbers):
    numbers = []
    for i in range(number_of_numbers):
        while True:
            num = input('Введіть число: ')
            try:
                num = int(num)
                numbers.append(num)
                break
            except ValueError:
                print('Введене вами значення не є числом.')
    return numbers


if __name__ == '__main__':
    nums = get_numbers(3)
    print(f'Мінімальне число зі списку {nums}: {min(nums)}')

