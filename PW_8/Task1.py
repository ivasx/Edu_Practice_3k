while True:
    fullname = input('Введіть прізвище, ім’я та по-батькові через пробіл: ').split()
    if len(fullname) == 3:
        name, middle_name = fullname[1], fullname[2]
        print(f'Ім’я: {name.capitalize()}')
        print(f'Кількість букв у третьому слові (по-батькові): {len(middle_name)}')
        break
    print('Будь ласка, введіть рівно три слова: прізвище, ім’я та по-батькові.')
