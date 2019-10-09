# 3x - ln(x) = 5
# d/dx = 3 - 1/x

# дихотомический метод и метод релаксации

# roots x1 = 0.0067843... x2 = 1.8764284...

import numpy as np

epsilon = 10 ** -10


def f(x: float):  # изначальная функция
    return 3 * x - np.log(x) - 5


def ddx(x: float):  # производная
    return 3 - 1 / x


def dichotomy(left: float, right: float):  # дихотомия
    x = (left + right) / 2
    while abs(f(x)) > epsilon:
        x = (left + right) / 2
        if f(x) * f(right) > 0:
            right = x
        else:
            left = x
    return (left + right) / 2


def relax(left: float, right: float):  # релаксация
    x, t, tau = 0, 0, 0
    t = (left + right) / 2
    if ddx(left) < 0 and ddx(right) < 0:
        tau = 2 / abs(ddx(left) + ddx(right))
    elif ddx(left) > 0 and ddx(right) > 0:
        tau = -2 / abs(ddx(left) + ddx(right))
    while abs(f(t)) > epsilon:
        x = t
        t = x + tau * f(x)
    return t


print('Дихатомический метод')
print(f'Первый корень = {dichotomy(0, 1)}')
print(f'Второй корень = {dichotomy(1, 5)}')

print('Метод релаксации')
print(f'Первый корень = {relax(10 ** -6, 0.3)}')
print(f'Второй корень = {relax(0.5, 5)}')
