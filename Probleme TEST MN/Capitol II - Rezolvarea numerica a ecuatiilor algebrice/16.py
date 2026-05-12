import math

f  = lambda x: x * math.exp(x) - 2
df = lambda x: math.exp(x) * (1 + x)
x, eps = 1.0, 1e-6

print(f"{'iter':>5} {'x':>15} {'f(x)':>15} {'eroare':>15}")
for i in range(50):
    fx  = f(x)
    x_nou = x - fx / df(x)
    err   = abs(x_nou - x)
    print(f"{i:>5} {x_nou:>15.10f} {f(x_nou):>15.2e} {err:>15.2e}")
    x = x_nou
    if err < eps:
        break

print(f"\nRadacina: x = {x:.10f}, iteratii: {i+1}")