# f(x) = x^2 - 3, f'(x) = 2x
x, eps = 1.0, 1e-6

print(f"{'iter':>5} {'x':>15} {'eroare':>15}")
for i in range(20):
    x_nou = x - (x**2 - 3) / (2 * x)
    err   = abs(x_nou - x)
    print(f"{i:>5} {x_nou:>15.10f} {err:>15.2e}")
    x = x_nou
    if err < eps:
        break

import math
print(f"\nRezultat:  {x:.10f}")
print(f"Exact:     {math.sqrt(3):.10f}")
print(f"Eroare:    {abs(x - math.sqrt(3)):.2e}")