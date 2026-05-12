import numpy as np

A = np.array([[3,-1,0],[-1,4,-1],[0,-1,2]], dtype=float)
b = np.array([10, 0, 5], dtype=float)

I = np.linalg.solve(A, b)

print("Curentii in circuit:")
for i, val in enumerate(I):
    print(f"  I{i+1} = {val:.6f} A")

print(f"\nVerificare Ax-b: {np.linalg.norm(A @ I - b):.2e}")