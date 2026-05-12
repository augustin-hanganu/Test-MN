import numpy as np

A = np.array([[3,1,1],[1,4,1],[1,1,5]], dtype=float)
b = np.array([1, 2, 3], dtype=float)

n = len(b)
L = np.eye(n)
U = A.copy()

for k in range(n):
    for i in range(k+1, n):
        f = U[i, k] / U[k, k]
        L[i, k] = f
        U[i, k:] -= f * U[k, k:]

print("L =\n", np.round(L, 4))
print("U =\n", np.round(U, 4))

y = np.zeros(n)
for i in range(n):
    y[i] = b[i] - np.dot(L[i, :i], y[:i])

x = np.zeros(n)
for i in range(n-1, -1, -1):
    x[i] = (y[i] - np.dot(U[i, i+1:], x[i+1:])) / U[i, i]

print(f"\nSolutie: {x}")
print(f"Verificare: {np.linalg.norm(A @ x - b):.2e}")