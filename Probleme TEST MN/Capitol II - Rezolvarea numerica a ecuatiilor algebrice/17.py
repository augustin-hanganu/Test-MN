import math

g   = lambda x: math.cos(x)   # x = cos(x)
x, eps = 0.5, 1e-6

print(f"{'iter':>5} {'x':>15} {'eroare':>15}")
for i in range(100):
    x_nou = g(x)
    err   = abs(x_nou - x)
    print(f"{i:>5} {x_nou:>15.10f} {err:>15.2e}")
    x = x_nou
    if err < eps:
        break

print(f"\nRadacina: x = {x:.10f}, iteratii: {i+1}")
print(f"Verificare: cos({x:.6f}) = {math.cos(x):.10f}")