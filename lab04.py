from copy import copy
from typing import List

import numpy as np

matrix = np.array([
    [7.4, 2.2, -3.7, -0.7],
    [1.6, 4.8, -8.5, 4.5],
    [4.7, 7.0, -6.0, 6.6],
    [5.9, 2.7, 4.9, -6.3]
])

coefficients = np.array([2, 4, 6, 8], dtype=float)

correct_res = np.linalg.solve(matrix, coefficients)


def gause_method(m: np.ndarray, c: np.ndarray):
    m = np.array(m)
    c = np.array(c)
    for i in range(m.shape[0]):
        for j in range(i + 1, m.shape[0]):
            # print(m[j][i])
            c[j] -= c[i] * m[j][i] / m[i][i]
            m[j] -= m[j][i] / m[i][i] * m[i]
    for i in range(m.shape[0]):
        c[i] /= m[i][i]
        m[i] /= m[i][i]
    x = np.zeros(m.shape[0])
    for i in range(m.shape[0] - 1, -1, -1):
        x[i] = c[i]
        for j in range(m.shape[0] - 1, i, -1):
            x[i] -= m[i][j] * x[j]
    return x


def fast_down(m, c, epsilon):
    g: np.array = np.dot(m.transpose(), c)
    B: np.array = np.dot(m.transpose(), m)
    # print(B, g, sep='\n')
    n = 0
    x: List[np.array] = [np.zeros(B.shape[0])]
    r: List = [np.dot(B, x[0]) - g]
    # print(epsilon)
    while n == 0 or not (np.sqrt(np.dot(r[-1], r[-1])) < epsilon and np.sqrt(np.dot(x[-1] - x[-2], x[-1] - x[-2])) < epsilon):
        tau = np.dot(r[-1], r[-1]) / np.dot(np.dot(B, r[-1]), r[-1])
        x.append(x[-1] - tau * r[-1])
        r.append(np.dot(B, x[-1]) - g)
        n += 1

    return x[-1], n


def conjugate_gradient(A, c, epsilon):
    A = np.array(copy(A))
    g = np.dot(A.transpose(), c)
    A = np.dot(A.transpose(), A)

    x: List[np.array] = [np.zeros(A.shape[0])]
    r: List[np.array] = [g - np.dot(A, x[0])]
    z: List[np.array] = [r[0]]

    n = 0
    while np.sqrt(np.dot(r[-1], r[-1])) / np.sqrt(np.dot(g, g)) > epsilon:
        alpha = np.dot(r[-1], r[-1]) / np.dot(np.dot(A, z[-1]), z[-1])
        x.append(x[-1] + alpha * z[-1])
        r.append(r[-1] - alpha * np.dot(A, z[-1]))
        beta = np.dot(r[-1], r[-1]) / np.dot(r[-2], r[-2])
        z.append(r[-1] + beta * z[-1])
        n += 1

    return x[-1], n


if __name__ == '__main__':
    print('\t\t\t\t\tПравильный ответ\n', correct_res)
    for i in range(2, 8):
        res = conjugate_gradient(matrix, coefficients, 10 ** -i)
        print(f'{res[1]}\t {res[0]} {10 ** -i}')
