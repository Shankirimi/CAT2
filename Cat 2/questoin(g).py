def trapezoidal_rule(f, a, b, n):
    h = (b - a) / n
    integral = 0.5 * (f(a) + f(b))
    for i in range(1, n):
        integral += f(a + i * h)
    integral *= h
    return integral

def f(x):
    return x**2

a = 0
b = 6
n = 12
print(trapezoidal_rule(f, a, b, n))
