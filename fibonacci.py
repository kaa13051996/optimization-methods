from math import sqrt
from time import time
# var5
start_time = time()
a, b = 0, 3
epsilon = 0.001

def generate_fibonacci(n):
    return (((1 + sqrt(5)) / 2) ** n - ((1 - sqrt(5)) / 2) ** n) / sqrt(5)

def search_n(a, b, epsilon):
    num = (b-a)/epsilon
    n = 1
    while (num > generate_fibonacci(n)):
        n+=1
    return n-2

def f(x):
    return 20*(x-1)**2+95

n = search_n(0, 3, 0.001)
print('Количество итераций: {0}'.format(n))

for k in range(1, n+1):
    inc = b - a
    if k==n:
        x_1 = a + (generate_fibonacci(1) / generate_fibonacci(n - k + 2)) * inc
        x_1 = a + (generate_fibonacci(2) / generate_fibonacci(n - k + 2)) * inc
    else:
        x_1 = a+(generate_fibonacci(n-k+1)/generate_fibonacci(n-k+3))*inc
        x_2 = a+(generate_fibonacci(n-k+2)/generate_fibonacci(n-k+3))*inc
    fun_1, fun_2 = f(x_1), f(x_2)
    if fun_2>fun_1:
        a, b = a, x_2
    else:
        a, b = x_1, b

print('a={0}, b={1}'.format(a, b))
print('Min: ',(a+b)/2)
print("--- %s seconds ---" % (time() - start_time))
