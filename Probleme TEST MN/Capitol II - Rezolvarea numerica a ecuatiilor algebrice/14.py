import math

f   = lambda x: x**3 - x - 2
a, b, eps = 1.0, 2.0, 1e-8

n_teoretic = math.ceil(math.log2((b - a) / eps))
print(f"Numar iteratii teoretic: ceil(log2({b-a}/{eps})) = {n_teoretic}")

it = 0
while (b - a) / 2 > eps:
    m = (a + b) / 2
    if f(a) * f(m) < 0:
        b = m
    else:
        a = m
    it += 1

print(f"Numar iteratii efectiv:  {it}")
print(f"Radacina: x = {(a+b)/2:.10f}")