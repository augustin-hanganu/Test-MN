import numpy as np

# Punctele si greutatile Gauss-Legendre pe [-1,1]
t = [-1/np.sqrt(3), 1/np.sqrt(3)]
w = [1, 1]

# Schimbare variabila: [a,b] -> [-1,1]
a, b = -1, 1
f = lambda x: np.exp(x)

rezultat = (b-a)/2 * sum(w[i] * f((a+b)/2 + (b-a)/2 * t[i]) for i in range(2))
exact    = np.e - np.exp(-1)

print(f"Gauss-Legendre 2 puncte: {rezultat:.8f}")
print(f"Exact:                   {exact:.8f}")
print(f"Eroare:                  {abs(rezultat - exact):.2e}")