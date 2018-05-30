from sympy import *
from time import time

start_time = time()


def f(x_1, x_2):
    return pow(x_1 + 3, 2) + 20 * pow(x_2 - 1, 2) + 95


x_1, x_2 = symbols('x_1 x_2')
dif = {}
dif[0] = diff(f(x_1, x_2), x_1)
dif[1] = diff(f(x_1, x_2), x_2)
print('Производные функции {0}: {1}'.format(f(x_1, x_2), dif))

x_begin = [5, 5, f(5, 5)]
x_mass = {0: x_begin}
t = [0.01]
epsilon = 0.001
max_iter = 1000
print('t = {0}'.format(t[0]))

count = 2
for i in range(1, count):
    a = round(x_mass[i - 1][0] - t[0] * dif[0]._args[0] * x_mass[i - 1][0], 4)
    b = round(x_mass[i - 1][1] - t[0] * dif[1]._args[0] * x_mass[i - 1][1], 4)
    var = round(dif[0]._args[0] * a + dif[1]._args[0] * b)
    x_mass[i] = [a, b, var]
    if (var < epsilon) or count == max_iter:
        break
    count += 1

print(x_mass)

print("--- {0} seconds ---".format(time() - start_time))
