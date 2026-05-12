import numpy as np

A = np.array([[4,1],[1,3]], dtype=float)

# Ecuatia caracteristica: lambda^2 - tr(A)*lambda + det(A) = 0
tr  = np.trace(A)
det = np.linalg.det(A)
print(f"tr(A) = {tr}, det(A) = {det}")
print(f"Ecuatie: λ² - {tr}λ + {det:.0f} = 0")

discriminant = tr**2 - 4*det
l1 = (tr + np.sqrt(discriminant)) / 2
l2 = (tr - np.sqrt(discriminant)) / 2
print(f"\nValori proprii: λ1={l1:.6f}, λ2={l2:.6f}")

# Vectori proprii
for lam in [l1, l2]:
    B = A - lam * np.eye(2)
    v = np.array([-B[0,1], B[0,0]])
    v = v / np.linalg.norm(v)
    print(f"λ={lam:.4f} → vector propriu: {v}")

print(f"\nVerificare numpy: {np.linalg.eigvals(A)}")