import math

f1  = lambda x: x * math.exp(x) - 2
df1 = lambda x: math.exp(x) * (1 + x)
f2  = lambda x: math.cos(x) - x
df2 = lambda x: -math.sin(x) - 1

def bisectie(f, a, b, eps=1e-6):
    it = 0
    while (b - a) / 2 > eps:
        m = (a + b) / 2
        if f(a) * f(m) < 0: b = m
        else: a = m
        it += 1
    return (a + b) / 2, it

def secanta(f, x0, x1, eps=1e-6):
    for i in range(100):
        x2 = x1 - f(x1) * (x1 - x0) / (f(x1) - f(x0))
        if abs(x2 - x1) < eps: return x2, i+1
        x0, x1 = x1, x2
    return x2, i+1

def newton(f, df, x0, eps=1e-6):
    for i in range(100):
        x1 = x0 - f(x0) / df(x0)
        if abs(x1 - x0) < eps: return x1, i+1
        x0 = x1
    return x1, i+1

print("=== f(x) = xe^x - 2 ===")
r, it = bisectie(f1, 0, 1);        print(f"Bisectie:      x={r:.8f}, iter={it}")
r, it = secanta(f1, 0, 1);         print(f"Secanta:       x={r:.8f}, iter={it}")
r, it = newton(f1, df1, 1);        print(f"Newton-Raphson:x={r:.8f}, iter={it}")

print("\n=== f(x) = cos(x) - x ===")
r, it = bisectie(f2, 0, 1);        print(f"Bisectie:      x={r:.8f}, iter={it}")
r, it = secanta(f2, 0, 1);         print(f"Secanta:       x={r:.8f}, iter={it}")
r, it = newton(f2, df2, 0.5);      print(f"Newton-Raphson:x={r:.8f}, iter={it}")