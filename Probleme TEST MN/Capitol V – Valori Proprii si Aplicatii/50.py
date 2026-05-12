import numpy as np

def F(v):
    x, y = v
    return np.array([x**2 + y**2 - 4,
                     np.exp(x) + y - 1])

def jacobian_numeric(F, v, h=1e-8):
    n  = len(v)
    m  = len(F(v))
    J  = np.zeros((m, n))
    for j in range(n):
        e      = np.zeros(n)
        e[j]   = h
        J[:, j] = (F(v + e) - F(v - e)) / (2*h)
    return J

v0 = np.array([1.0, 1.5])

J_numeric  = jacobian_numeric(F, v0)
J_analitic = np.array([[2*v0[0], 2*v0[1]],
                        [np.exp(v0[0]), 1]])

print("Jacobian numeric:")
print(np.round(J_numeric, 8))
print("\nJacobian analitic:")
print(np.round(J_analitic, 8))
print(f"\nEroare: {np.linalg.norm(J_numeric - J_analitic):.2e}")