import numpy as np

f = lambda x: np.exp(x)
a, b, n = 0, 1, 4

x = np.linspace(a, b, n+1)
h = (b - a) / n

rezultat = h/2 * (f(x[0]) + 2*np.sum(f(x[1:-1])) + f(x[-1]))
exact    = np.e - 1

print(f"Trapez (n={n}): {rezultat:.8f}")
print(f"Exact:          {exact:.8f}")
print(f"Eroare:         {abs(rezultat - exact):.2e}")