def get_n():
    while True:
        n = input('Введіть число n: ')
        try:
            n = int(n)
            break
        except ValueError:
            print('Введене вами значення не є числом.')
    return n

def replace_a_o(n):
    while True:
        line = input(f'Введіть рядок (довжина не може перевищувати ({n}) символів: ')
        if len(line) <= n:
            break
        else:
            print(f'У вашому рядку {len(line)} символів, це більше ніж {n}.')

    replace_map = {
        'а': 'о',
        'А': 'О',
        'a': 'o',
        'A': 'O',
    }

    if not any(ch in replace_map for ch in line):
        print('У рядку немає букв "а".')
        return line

    a_found = False
    result = []

    for i in line:
        if i in replace_map:
            if not a_found:
                result.append(i)
                a_found = True
            else:
                result.append(replace_map[i])
        else:
            result.append(i)

    return ''.join(result)

if __name__ == '__main__':
    n = get_n()
    print(replace_a_o(n))