from scipy.optimize import minimize_scalar

def f(x):
    return 20*(x-1)**2+95

res = minimize_scalar(f, bracket=(0, 3), method='Golden', tol=0.001)
print(res)