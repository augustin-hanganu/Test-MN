import numpy as np

f  = lambda x: np.sin(x)
x0 = np.pi / 4
h  = 0.1

# Derivata 1 - diferente finite centrate
f_prim = (f(x0 + h) - f(x0 - h)) / (2*h)

# Derivata 2 - diferente finite centrate
f_bis  = (f(x0 + h) - 2*f(x0) + f(x0 - h)) / h**2

print(f"f'(π/4)  numeric:  {f_prim:.8f}")
print(f"f'(π/4)  exact:    {np.cos(x0):.8f}")
print(f"Eroare f':         {abs(f_prim - np.cos(x0)):.2e}")

print(f"\nf''(π/4) numeric:  {f_bis:.8f}")
print(f"f''(π/4) exact:    {-np.sin(x0):.8f}")
print(f"Eroare f'':        {abs(f_bis - (-np.sin(x0))):.2e}")