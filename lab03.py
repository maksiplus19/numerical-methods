# Вариант 9
# 5x - 6y + 20lgx + 16 = 0
# 2x + y - 10lgy - 4 = 0
import numpy as np

perception = 5
epsilon = 10 ** -perception
h = 10**-perception


def f(x: float, y: float):
    return 5 * x - 6 * y + 20 * np.log10(x) + 16


def g(x: float, y: float):
    return 2 * x + y - 10 * np.log10(y) - 4


def a(x: float):
    return 20 / (x * np.log(10)) + 5


def b():
    return -6


def c():
    return 2


def d(y: float):
    return 1 - 10 / (y * np.log(10))


def dfdx(x: float, y: float):
    return (f(x + h, y) - f(x, y)) / h


def dfdy(x: float, y: float):
    return (f(x, y + h) - f(x, y)) / h


def dgdx(x: float, y: float):
    return (g(x + h, y) - g(x, y)) / h


def dgdy(x: float, y:float):
    return (g(x, y + h) - g(x, y)) / h


def jacobi_matrix(x: float, y: float) -> np.array:
    arr = np.array([[a(x), b()], [c(), d(y)]])
    return arr


def jacobi_matrix_numerical(x: float, y: float):
    arr = np.array([[dfdx(x, y), dfdy(x, y)], [dgdx(x, y), dgdy(x, y)]])
    return arr


def F(x: float, y: float):
    arr = np.array([f(x, y), g(x, y)])
    return arr


def get_delta(W: np.array, F: np.array):
    res = np.linalg.tensorsolve(W, -F)
    return res


if __name__ == '__main__':
    x_n, y_n = 3, 3
    old_x, old_y = 0, 0
    k = 0

    while np.sqrt(f(x_n, y_n) ** 2 + g(x_n, y_n) ** 2) > epsilon \
            and np.sqrt((x_n - old_x) ** 2 + (y_n - old_y) ** 2) > epsilon:
        old_x, old_y = x_n, y_n
        delta = get_delta(jacobi_matrix(old_x, old_y), F(old_x, old_y))
        x_n, y_n = old_x + delta[0], old_y + delta[1]
        k += 1

    print('Аналитические производные\nx = {:.6}\ty = {:.6}\tИтераций {}'.format(x_n, y_n, k))

    x_n, y_n = 3, 3
    old_x, old_y = 0, 0
    k = 0

    while np.sqrt(f(x_n, y_n) ** 2 + g(x_n, y_n) ** 2) > epsilon \
            and np.sqrt((x_n - old_x) ** 2 + (y_n - old_y) ** 2) > epsilon:
        old_x, old_y = x_n, y_n
        delta = get_delta(jacobi_matrix_numerical(old_x, old_y), F(old_x, old_y))
        x_n, y_n = old_x + delta[0], old_y + delta[1]
        k += 1

    print('Численные производные\nx = {:.6}\ty = {:.6}\tИтераций {}'.format(x_n, y_n, k))
