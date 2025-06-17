import math

def input_arg():
    try:
        x = float(input("Введіть значення x: "))
        y = float(input("Введіть значення y: "))
        return x, y
    except ValueError:
        print('Введено некоректне значення одного з елементів, спробуйте знову.')
        input_arg()
        return None


def u_function(x, y):
    return x**2 + y**2

def v_function(u):
    return (1 + u**2) * math.log(u)**2

if __name__ == '__main__':
    x, y = input_arg()
    u = u_function(x, y)
    try:
        v = v_function(u)
        print(f"u = {u}")
        print(f"v = {v}")
    except ValueError as error:
        print(f"Помилка: {error}")