import math

def formula_standard(p):
    delta = p**2 - 1
    x1 = p + math.sqrt(delta)
    x2 = p - math.sqrt(delta)
    return x1, x2

def formula_stabila(p):
    delta = p**2 - 1
    x1 = p + math.sqrt(delta)
    x2 = 1 / x1          # evita scaderea numerelor apropiate
    return x1, x2

print(f"{'p':>8} {'x2_standard':>20} {'x2_stabila':>20}")
for p in [10, 100, 1000, 10000, 100000]:
    x1_s, x2_s = formula_standard(p)
    x1_st, x2_st = formula_stabila(p)
    print(f"{p:>8} {x2_s:>20.10f} {x2_st:>20.10f}")

print("\nConcluzie: Formula stabila evita pierderea de cifre semnificative")
print("la scaderea numerelor foarte apropiate (p >> 1)!")


def formula1(P):
    a = 1
    b = -2.0 * P
    c = 1
    delta = b**2 - 4 * a * c
    x1 = (-b + math.sqrt(delta)) / 2
    x2 = (-b - math.sqrt(delta)) / 2
    return x1,x2

def formula2(P):
    a = 1
    b = -2.0 * P
    c = 1
    delta = b**2 - 4 * a * c
    sqrt_delta = math.sqrt(delta)
    q = -0.5 * (b + math.copysign(sqrt_delta, b))
    x1 = q / a
    x2 = c / q
    return x1, x2

print(f"{'p':>10} {'x2_stand':>20} {'x2_stab':>20}")
for P in [10,100,1000,10000,100000]:
    x1_ss , x2_ss = formula1(P)
    x1_stt, x2_stt = formula2(P)
    print(f"{p:>10} {x2_ss:>20} {x2_stt:>20}")