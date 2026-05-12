import math

f   = lambda x: x * math.exp(x) - 2
a, b, eps = 0.0, 1.0, 1e-6

print(f"{'iter':>5} {'a':>12} {'b':>12} {'mijloc':>12} {'f(m)':>12}")
it = 0
while (b - a) / 2 > eps:
    m = (a + b) / 2
    print(f"{it:>5} {a:>12.8f} {b:>12.8f} {m:>12.8f} {f(m):>12.2e}")
    if f(a) * f(m) < 0:
        b = m
    else:
        a = m
    it += 1

print(f"\nRadacina: x = {(a+b)/2:.8f}, iteratii: {it}")