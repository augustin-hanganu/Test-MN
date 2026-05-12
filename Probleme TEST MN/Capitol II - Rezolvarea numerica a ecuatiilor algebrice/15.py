import math

f   = lambda x: x * math.exp(x) - 2
x0, x1, eps = 0.0, 1.0, 1e-6

print(f"{'iter':>5} {'x':>15} {'f(x)':>15}")
for i in range(50):
    f0, f1 = f(x0), f(x1)
    x2 = x1 - f1 * (x1 - x0) / (f1 - f0)
    print(f"{i:>5} {x2:>15.10f} {f(x2):>15.2e}")
    if abs(x2 - x1) < eps:
        break
    x0, x1 = x1, x2

print(f"\nRadacina: x = {x2:.10f}, iteratii: {i+1}")