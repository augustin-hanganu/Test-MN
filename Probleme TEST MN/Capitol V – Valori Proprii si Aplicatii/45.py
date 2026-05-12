import numpy as np
import matplotlib.pyplot as plt

L, n = 1.0, 4
h    = L / (n + 1)
x    = np.linspace(h, L-h, n)  # noduri interioare

q = lambda xi: 100 * np.sin(np.pi * xi)

# Sistem tridiagonal: -T(i-1) + 2T(i) - T(i+1) = h^2 * q(xi)
A = np.zeros((n, n))
b = np.array([h**2 * q(xi) for xi in x])

for i in range(n):
    A[i, i] = 2
    if i > 0:   A[i, i-1] = -1
    if i < n-1: A[i, i+1] = -1

T = np.linalg.solve(A, b)

x_plot = np.concatenate([[0], x, [L]])
T_plot = np.concatenate([[0], T, [0]])

print(f"{'x':>8} {'T(x)':>12}")
for xi, Ti in zip(x_plot, T_plot):
    print(f"{xi:>8.4f} {Ti:>12.6f}")

plt.plot(x_plot, T_plot, 'bo-')
plt.title('Problema 45: Distributia temperaturii')
plt.xlabel('x'); plt.ylabel('T(x)')
plt.grid(True); plt.tight_layout(); plt.show()