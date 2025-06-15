machinegram = [
    ('№ п/п', 'Табельний', 'Нараховано', 'Заборгованiсть', 'До видачi'),
    (1, 10001, 14200, 1200, 13000),
    (2, 10002, 18900, 2500, 16400),
    (3, 10003, 9900, 0, 9900),
    (4, 10004, 11200, 600, 10600),
    (5, 10005, 8600, 860, 7740)
]

def show_machinegram(info_list, num_lines=1):
    if num_lines > len(info_list):
        num_lines = len(info_list) - 1

    for i in range(num_lines + 1):
        info = info_list[i]
        print(f'{info[0]:<15}'
              f'{info[1]:<15}'
              f'{info[2]:<15}'
              f'{info[3]:<20}'
              f'{info[4]:<10}')

if __name__ == '__main__':
    show_machinegram(machinegram)
