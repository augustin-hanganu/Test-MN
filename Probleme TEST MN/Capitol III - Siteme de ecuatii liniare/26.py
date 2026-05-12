import numpy as np

U = np.array([[2,3,-1],[0,4,2],[0,0,5]], dtype=float)
y = np.array([5, 10, 15], dtype=float)

n = len(y)
x = np.zeros(n)
for i in range(n-1, -1, -1):
    x[i] = (y[i] - np.dot(U[i, i+1:], x[i+1:])) / U[i, i]

print(f"Solutie: {x}")
print(f"Verificare Ux-y: {np.linalg.norm(U @ x - y):.2e}")