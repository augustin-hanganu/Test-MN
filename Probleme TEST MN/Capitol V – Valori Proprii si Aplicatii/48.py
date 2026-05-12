import numpy as np

A = np.array([[4,1,0],[1,3,1],[0,1,2]], dtype=float)

print("Valori proprii prin metoda QR (iteratii):")
Ak = A.copy()
for i in range(100):
    Q, R = np.linalg.qr(Ak)
    Ak   = R @ Q

valori_proprii = np.diag(Ak)
print(f"Valori proprii QR:    {np.sort(valori_proprii)[::-1]}")
print(f"Verificare numpy:     {np.sort(np.linalg.eigvals(A))[::-1]}")