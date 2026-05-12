import numpy as np

L = np.array([[2,0,0],[3,4,0],[1,2,5]], dtype=float)
b = np.array([4, 11, 20], dtype=float)

n = len(b)
x = np.zeros(n)
for i in range(n):
    x[i] = (b[i] - np.dot(L[i, :i], x[:i])) / L[i, i]

print(f"Solutie: {x}")
print(f"Verificare Lx-b: {np.linalg.norm(L @ x - b):.2e}")