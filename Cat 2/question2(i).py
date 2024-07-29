x = symbols('x')
f = x**3 + 2*x**2 + x
df = diff(f, x)

print(df)
