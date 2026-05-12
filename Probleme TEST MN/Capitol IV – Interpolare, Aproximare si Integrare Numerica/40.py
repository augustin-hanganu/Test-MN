import numpy as np

f = lambda x: np.sin(x)
a, b = 0, np.pi
exact = 2.0  # integral sin(x) pe [0,pi]

def trapez(f, a, b, n):
    x = np.linspace(a, b, n+1)
    h = (b - a) / n
    return h/2 * (f(x[0]) + 2*np.sum(f(x[1:-1])) + f(x[-1]))

for n in [8, 16]:
    rez = trapez(f, a, b, n)
    print(f"n={n:>2}: rezultat={rez:.8f}, eroare={abs(rez-exact):.2e}")

print(f"\nExact: {exact}")
print("Eroarea scade de ~4x la dublarea lui n (ord. 2)")