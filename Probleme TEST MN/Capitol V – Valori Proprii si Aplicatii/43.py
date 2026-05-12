import numpy as np

A = np.array([[2,1],[1,2]], dtype=float)
v = np.array([1.0, 0.0])

print(f"{'iter':>5} {'lambda':>15} {'eroare':>12}")
lam_old = 0
for i in range(100):
    w   = A @ v
    lam = np.max(np.abs(w))
    v   = w / lam
    err = abs(lam - lam_old)
    print(f"{i:>5} {lam:>15.10f} {err:>12.2e}")
    if err < 1e-8:
        break
    lam_old = lam

print(f"\nValoare proprie maxima: {lam:.8f}")
print(f"Vector propriu:         {v}")
print(f"Verificare (analitic):  {np.linalg.eigvals(A)}")