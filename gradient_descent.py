from sympy import *
from time import time

start_time = time()

def f(x_1, x_2):
    return pow(x_1,2)+2*pow(x_2,2)

x_1, x_2 = symbols('x_1 x_2')
dif = {}
dif[0] = diff(f(x_1, x_2), x_1)
dif[1] = diff(f(x_1, x_2), x_2)
print('Производные функции {0}: {1}'.format(f(x_1, x_2), dif))

x_begin = [5, 4, f(5, 4)]
x_mass = {0: x_begin}
t = [0.001]
print('t = {0}'.format(t[0]))

for i in range(1, 5):
    a = round(x_mass[i - 1][0] - t[0] * dif[0]._args[0] * x_mass[i - 1][0], 4)
    b = round(x_mass[i - 1][1] - t[0] * dif[1]._args[0] * x_mass[i - 1][1], 4)
    fun = round(pow(a, 2) + 2 * pow(b, 2), 4)
    x_mass[i] = [a, b, fun]
print(x_mass)

print("--- %s seconds ---" % (time() - start_time))






