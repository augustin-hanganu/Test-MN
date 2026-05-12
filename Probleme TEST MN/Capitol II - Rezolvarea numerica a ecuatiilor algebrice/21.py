import numpy as np

# F1 = x^2 + y^2 - 4 = 0
# F2 = e^x + y - 1 = 0
def F(v):
    x, y = v
    return np.array([x**2 + y**2 - 4,
                     np.exp(x) + y - 1])

def J(v):
    x, y = v
    return np.array([[2*x,        2*y],
                     [np.exp(x),  1  ]])

v, eps = np.array([1.0, 1.5]), 1e-6

print(f"{'iter':>5} {'x':>15} {'y':>15} {'|F|':>12}")
for i in range(20):
    Fv  = F(v)
    nrm = np.linalg.norm(Fv)
    print(f"{i:>5} {v[0]:>15.10f} {v[1]:>15.10f} {nrm:>12.2e}")
    if nrm < eps: break
    v = v - np.linalg.solve(J(v), Fv)

print(f"\nSolutie: x={v[0]:.8f}, y={v[1]:.8f}")