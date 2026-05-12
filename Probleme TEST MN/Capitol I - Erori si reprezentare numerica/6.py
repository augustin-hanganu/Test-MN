import math

e_real = math.e
termen = 1.0
suma   = 1.0

print(f"{'N':>3} {'Suma':>15} {'Eroare absoluta':>18}")
print(f"{'0':>3} {suma:>15.10f} {abs(e_real - suma):>18.2e}")

for n in range(1, 6):
    termen /= n
    suma   += termen
    print(f"{n:>3} {suma:>15.10f} {abs(e_real - suma):>18.2e}")