import numpy as np

A = np.array([[4,1,-1,1],[1,5,2,0],[-1,2,6,1],[1,0,1,4]], dtype=float)
b = np.array([12, 8, 19, 11], dtype=float)

# Gauss cu pivotare partiala
n = len(b)
Ab = np.hstack([A, b.reshape(-1,1)])

for k in range(n):
    # pivotare
    max_row = np.argmax(np.abs(Ab[k:, k])) + k
    Ab[[k, max_row]] = Ab[[max_row, k]]
    # eliminare
    for i in range(k+1, n):
        factor = Ab[i, k] / Ab[k, k]
        Ab[i, k:] -= factor * Ab[k, k:]

# retrosubstitutie
x = np.zeros(n)
for i in range(n-1, -1, -1):
    x[i] = (Ab[i, -1] - np.dot(Ab[i, i+1:n], x[i+1:])) / Ab[i, i]

print(f"Solutie Gauss: {x}")
print(f"Verificare Ax-b: {np.linalg.norm(A @ x - b):.2e}")