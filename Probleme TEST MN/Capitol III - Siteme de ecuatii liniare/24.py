import numpy as np

A = np.array([[4,1,-1,1],[1,5,2,0],[-1,2,6,1],[1,0,1,4]], dtype=float)
b = np.array([12, 8, 19, 11], dtype=float)

n = len(b)
L = np.eye(n)
U = A.copy()

# Factorizare LU Crout
for k in range(n):
    for i in range(k+1, n):
        factor = U[i, k] / U[k, k]
        L[i, k] = factor
        U[i, k:] -= factor * U[k, k:]

print("=== Factorizare LU (Crout) ===")
print("L =\n", np.round(L, 4))
print("U =\n", np.round(U, 4))
print(f"\nVerificare L*U = A: {np.linalg.norm(L @ U - A):.2e}")

# Ly = b (substitutie directa)
y = np.zeros(n)
for i in range(n):
    y[i] = b[i] - np.dot(L[i, :i], y[:i])

print(f"\nSolutie y (Ly=b): {y}")

# Ux = y (retrosubstitutie)
x = np.zeros(n)
for i in range(n-1, -1, -1):
    x[i] = (y[i] - np.dot(U[i, i+1:], x[i+1:])) / U[i, i]

print(f"Solutie x (Ux=y): {x}")
print(f"\nVerificare Ax-b: {np.linalg.norm(A @ x - b):.2e}")