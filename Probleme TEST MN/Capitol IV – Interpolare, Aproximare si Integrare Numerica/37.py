import numpy as np

f = lambda x: np.exp(x)
a, b, n = 0, 1, 3  # n multiplu de 3

x = np.linspace(a, b, n+1)
h = (b - a) / n

rezultat = 3*h/8 * (f(x[0]) + 3*f(x[1]) + 3*f(x[2]) + f(x[3]))
exact    = np.e - 1

print(f"Simpson 3/8 (n={n}): {rezultat:.8f}")
print(f"Exact:               {exact:.8f}")
print(f"Eroare:              {abs(rezultat - exact):.2e}")