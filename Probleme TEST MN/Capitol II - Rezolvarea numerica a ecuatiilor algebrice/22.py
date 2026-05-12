import numpy as np

# Sistem 3x3 exemplu polynomial + exponential
def F(v):
    x, y, z = v
    return np.array([x**2 + y**2 + z**2 - 14,
                     x + y**2 - z - 4,
                     np.exp(x) - y - z - 1])

def J(v):
    x, y, z = v
    return np.array([[2*x,       2*y,  2*z ],
                     [1,         2*y,  -1  ],
                     [np.exp(x), -1,   -1  ]])

v, eps = np.array([1.0, 3.0, 1.0]), 1e-6

print(f"{'iter':>5} {'x':>12} {'y':>12} {'z':>12} {'|F|':>12}")
for i in range(20):
    Fv  = F(v)
    nrm = np.linalg.norm(Fv)
    print(f"{i:>5} {v[0]:>12.8f} {v[1]:>12.8f} {v[2]:>12.8f} {nrm:>12.2e}")
    if nrm < eps: break
    v = v - np.linalg.solve(J(v), Fv)

print(f"\nSolutie: x={v[0]:.8f}, y={v[1]:.8f}, z={v[2]:.8f}")