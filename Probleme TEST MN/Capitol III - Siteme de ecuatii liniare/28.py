import numpy as np

A = np.array([[2,1,-1],[-3,-1,2],[-2,1,2]], dtype=float)
b = np.array([8, -11, -3], dtype=float)

n = len(b)
Ab = np.hstack([A, b.reshape(-1,1)])

for k in range(n):
    max_row = np.argmax(np.abs(Ab[k:, k])) + k
    Ab[[k, max_row]] = Ab[[max_row, k]]
    for i in range(k+1, n):
        f = Ab[i, k] / Ab[k, k]
        Ab[i, k:] -= f * Ab[k, k:]

x = np.zeros(n)
for i in range(n-1, -1, -1):
    x[i] = (Ab[i, -1] - np.dot(Ab[i, i+1:n], x[i+1:])) / Ab[i, i]

print(f"Solutie: {x}")
print(f"Verificare Ax-b: {np.linalg.norm(A @ x - b):.2e}")