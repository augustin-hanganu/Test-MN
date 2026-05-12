import numpy as np

A = np.array([[6,2,1],[2,5,2],[1,2,4]], dtype=float)

# Verificare simetrica pozitiv definita
print(f"Simetrica: {np.allclose(A, A.T)}")
print(f"Valori proprii: {np.linalg.eigvals(A)}")
print(f"Pozitiv definita: {np.all(np.linalg.eigvals(A) > 0)}")

# Cholesky manual
n = len(A)
L = np.zeros((n, n))
for i in range(n):
    for j in range(i+1):
        s = np.dot(L[i, :j], L[j, :j])
        if i == j:
            L[i, j] = np.sqrt(A[i, i] - s)
        else:
            L[i, j] = (A[i, j] - s) / L[j, j]

print("\nL (Cholesky) =\n", np.round(L, 4))
print(f"Verificare L*L^T = A: {np.linalg.norm(L @ L.T - A):.2e}")