import math

# alpha, betta = 0.6, 0.4
# epsilon = 0.001

def f(x):
    return math.fabs(x - 2)

def golden(a, b, alpha = 0.6, betta = 0.4, epsilon = 0.001):
    inc = b-a
    x_alpha = a+alpha*inc
    x_betta = a+betta*inc
    fun_alpha, fun_betta = f(x_alpha), f(x_betta)
    if fun_betta>fun_alpha:
        a, b = x_betta, b
    else:
        a, b = a, x_alpha
    if inc<epsilon:
        return(a,b)
    else:
        golden(a,b)

print(golden(a = 0, b = 3))
