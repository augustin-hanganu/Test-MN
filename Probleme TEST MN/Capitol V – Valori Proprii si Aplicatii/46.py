import numpy as np

def F(v):
    x, y = v
    return np.array([x**2 + y**2 - 4,
                     np.exp(x) + y - 1])

def J(v):
    x, y = v
    return np.array([[2*x, 2*y],
                     [np.exp(x), 1]])

v = np.array([1.0, 1.5])
B = J(v)  # Jacobian initial

print(f"{'iter':>5} {'x':>12} {'y':>12} {'|F|':>12}")
for i in range(20):
    Fv  = F(v)
    nrm = np.linalg.norm(Fv)
    print(f"{i:>5} {v[0]:>12.8f} {v[1]:>12.8f} {nrm:>12.2e}")
    if nrm < 1e-8: break

    s  = -np.linalg.solve(B, Fv)
    v_nou = v + s
    y_vec = F(v_nou) - Fv
    # Update Broyden
    B = B + np.outer((y_vec - B @ s), s) / np.dot(s, s)
    v = v_nou

print(f"\nSolutie: x={v[0]:.8f}, y={v[1]:.8f}")