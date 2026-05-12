import numpy as np

A_bun  = np.array([[4,1],[1,3]], dtype=float)
A_slab = np.array([[1,1],[1,1.0001]], dtype=float)

b      = np.array([1, 1], dtype=float)
b_pert = np.array([1.001, 1.001], dtype=float)  # perturbatie 0.1%

for nume, A in [("A_bun", A_bun), ("A_slab", A_slab)]:
    x      = np.linalg.solve(A, b)
    x_pert = np.linalg.solve(A, b_pert)
    cond   = np.linalg.cond(A)
    eroare = np.linalg.norm(x_pert - x) / np.linalg.norm(x)
    print(f"{nume}: cond={cond:.2f}, eroare relativa solutie={eroare:.6f} ({eroare*100:.2f}%)")