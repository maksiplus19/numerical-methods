import numpy as np

while True:
    try:
        x = float(input('Enter x = '))
    except ValueError:
        break
    amount = 0.0
    res = 4 / (np.sqrt(1 - 4 * x) * (1 + np.sqrt(1 - 4 * x)) ** 2)
    k = 0
    a = 1

    while np.abs(amount - res) > 10 ** -10:
        amount += a
        a *= (2 * k + 3) * (2 * k + 4) * x / ((k + 1) * (k + 3))
        k += 1

    print(f'k = {k}\nsum = {amount}\nres = {res}')
