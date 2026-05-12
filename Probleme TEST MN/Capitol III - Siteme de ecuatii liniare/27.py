import numpy as np

A = np.array([[10,-1,2,0],[-1,11,-1,3],[2,-1,10,-1],[0,3,-1,8]], dtype=float)
b = np.array([6, 25, -11, 15], dtype=float)

x, eps = np.zeros(4), 1e-6

print(f"{'iter':>5} {'x1':>12} {'x2':>12} {'x3':>12} {'x4':>12}")
for it in range(100):
    x_nou = np.array([(b[i] - np.dot(A[i], x) + A[i,i]*x[i]) / A[i,i] for i in range(4)])
    print(f"{it:>5} {x_nou[0]:>12.6f} {x_nou[1]:>12.6f} {x_nou[2]:>12.6f} {x_nou[3]:>12.6f}")
    if np.linalg.norm(x_nou - x) < eps:
        break
    x = x_nou

print(f"\nSolutie: {x_nou}")