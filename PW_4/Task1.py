import math

nums_inp = input('Введіть числа через пробіл: ').split()

def validate_numbers(*args):
    nums = []
    for n in args:
        if len(nums) == 10:
            break

        try:
            n = int(n)
            if n % 3 == 0:
                nums.append(n)
        except ValueError:
            pass

    nums.sort()
    return nums

def counter(num_list):
    positives = [n for n in num_list if n >= 0]
    negatives = [n for n in num_list if n < 0]

    p_total = sum(positives)
    n_total = sum(negatives)
    p_count = len(positives)
    n_count = len(negatives)

    p_avg = p_total / p_count if p_count else 0
    n_avg = n_total / n_count if n_count else 0
    t_avg = (p_total + n_total) / (p_count + n_count) if (p_count + n_count) else 0
    n_prod = math.prod(negatives) if n_count else 0

    return (f'Масив {num_list}'
            f'\nКількість додатніх чисел: {p_count}, їх середнє арифметичне {p_avg}'
            f'\nЇхня сума: {p_total}'
            f'\nКількість від\'ємних чисел: {n_count}'
            f'\nЇхній добуток: {n_prod}, їх середнє арифметичне: {n_avg}'
            f'\nСереднє арифметичне усього масиву: {t_avg}')


if __name__ == '__main__':
    print(counter(validate_numbers(*nums_inp)))
