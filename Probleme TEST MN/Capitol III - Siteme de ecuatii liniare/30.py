import numpy as np

A = np.array([[1,1],[1,1.0001]], dtype=float)
b = np.array([2, 2.0001], dtype=float)
b_pert = b * 1.001  # perturbatie 0.1%

x      = np.linalg.solve(A, b)
x_pert = np.linalg.solve(A, b_pert)

print(f"Solutie originala:   {x}")
print(f"Solutie perturbata:  {x_pert}")
print(f"Conditie A:          {np.linalg.cond(A):.2e}")
print(f"Eroare relativa sol: {np.linalg.norm(x_pert-x)/np.linalg.norm(x):.4f}")
print("\nMatrice slab conditionata → perturbatie mica in b => eroare mare in x!")