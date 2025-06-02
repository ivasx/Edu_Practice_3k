print('Джон народився у 1942 році.')
while True:
    current_year = input('Введіть який зараз рік: ')
    if current_year.isdigit():
        current_year = int(current_year)
        break
    else:
        print('Введений вами рік не є числом, спробуйте знову. ')

print(f'Зараз Джону {current_year - 1942} роки.' if current_year >= 1942 else 'Джон ще не народився.')

