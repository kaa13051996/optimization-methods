# from random import uniform
from math import fabs
from time import time

# var5
start_time = time()
a, b = 0, 3
epsilon = 0.001
# delta = uniform(0, epsilon)
delta = 7.110642666101863e-05


def f(x):
    return 20 * (x - 1) ** 2 + 95


while (fabs(b - a) >= epsilon):
    x_1 = (a + b) / 2 - delta
    x_2 = (a + b) / 2 + delta
    fun_1, fun_2 = f(x_1), f(x_2)
    if fun_2 > fun_1:
        a, b = a, x_2
    else:
        a, b = x_1, b

print('a={0}, b={1}'.format(a, b))
print('Min: ', (a + b) / 2)
print("--- {0} seconds ---".format(time() - start_time))
