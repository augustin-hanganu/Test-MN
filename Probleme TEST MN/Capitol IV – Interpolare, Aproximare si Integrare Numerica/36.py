import numpy as np

f = lambda x: np.exp(x)
a, b, n = 0, 1, 4  # n par

x = np.linspace(a, b, n+1)
h = (b - a) / n

rezultat = h/3 * (f(x[0]) + 4*np.sum(f(x[1:-1:2])) + 2*np.sum(f(x[2:-2:2])) + f(x[-1]))
exact    = np.e - 1

print(f"Simpson 1/3 (n={n}): {rezultat:.8f}")
print(f"Exact:               {exact:.8f}")
print(f"Eroare:              {abs(rezultat - exact):.2e}")