from time import time

start_time = time()
a, b = -2, 2
alpha, betta = 0.618, 0.382
epsilon = 0.001

def f(x):
    return 20 * (x - 1) ** 2 + 95

inc = b - a
while (inc >= epsilon):
    x_alpha = a + alpha * inc
    x_betta = a + betta * inc
    fun_alpha, fun_betta = f(x_alpha), f(x_betta)
    if fun_betta > fun_alpha:
        a, b = x_betta, b
    else:
        a, b = a, x_alpha
    inc = b - a

print('a={0}, b={1}'.format(a, b))
print('Min: ', (a + b) / 2)
print("--- {0} seconds ---".format(time() - start_time))
