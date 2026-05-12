import numpy as np

A = np.array([[5,1,1],[1,7,-1],[-1,1,6]], dtype=float)
b = np.array([10, 12, 8], dtype=float)

x, eps = np.zeros(3), 1e-6

print(f"{'iter':>5} {'x1':>12} {'x2':>12} {'x3':>12}")
for it in range(100):
    x_old = x.copy()
    for i in range(3):
        x[i] = (b[i] - np.dot(A[i], x) + A[i,i]*x[i]) / A[i,i]
    print(f"{it:>5} {x[0]:>12.6f} {x[1]:>12.6f} {x[2]:>12.6f}")
    if np.linalg.norm(x - x_old) < eps:
        break

print(f"\nSolutie: {x}")
print(f"Verificare: {np.linalg.norm(A @ x - b):.2e}")