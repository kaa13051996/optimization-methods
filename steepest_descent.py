from sympy import diff, symbols, solve
from time import time

start_time = time()

def f(x_1, x_2):
    return pow(x_1 + 3, 2) + 20 * pow(x_2 - 1, 2) + 95

def gradient_descent(x_mass, epsilon, max_iter):
    var_begin = 1
    count = 1
    while var_begin > epsilon and count < max_iter:
        t = search_t(x_mass[count - 1])
        a = round(x_mass[count - 1][0] - t * dif[0].subs({x_1: x_mass[count - 1][0]}), 4)
        b = round(x_mass[count - 1][1] - t * dif[1].subs({x_2: x_mass[count - 1][1]}), 4)
        var_end = dif[0].subs({x_1: a}) + dif[1].subs({x_2: b})
        if (var_begin != var_end):
            var_begin = var_end
            x_mass[count] = [a, b]
            count += 1
        else:
            print('Точность далее не изменится! Программа завершила работу с точностью {0}'.format(var_begin))
            break
    return (x_mass[count - 1], count, var_begin)

def search_t(x_mass):
    t = symbols('t')
    fi_a = x_mass[0] - t * dif[0].subs({x_1: x_mass[0]})
    fi_b = x_mass[1] - t * dif[1].subs({x_2: x_mass[1]})
    fi = f(fi_a, fi_b)
    rezult = float(solve([diff(fi, t)]).get(t))
    return rezult

x_1, x_2 = symbols('x_1 x_2')
dif = {}
dif[0] = diff(f(x_1, x_2), x_1)
dif[1] = diff(f(x_1, x_2), x_2)
print('Производные функции:\n- по х_1 = {0}\n- по х_2 = {1}'.format(dif[0], dif[1]))

result = gradient_descent(x_mass={0: [-2, 2]}, epsilon=0.001, max_iter=10000)

print('Минимум функции на {0} итерации с точностью {1} в точке: {2}'.format(result[1], result[2], result[0]))
print("--- {0} seconds ---".format(time() - start_time))
