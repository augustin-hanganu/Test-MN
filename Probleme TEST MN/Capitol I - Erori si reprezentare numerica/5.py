# I_n = 1/n - (9/2)*I_(n-1)
# I_0 exacta vs aproximata

def calc_In(I0, n):
    I = I0
    for k in range(1, n+1):
        I = 1/k - (9/2) * I
    return I

I0_exact = 0.1003353477
I0_aprox = 0.10034

n = 7
rez_exact = calc_In(I0_exact, n)
rez_aprox = calc_In(I0_aprox, n)

print(f"I7 cu I0 exacta:      {rez_exact:.8f}")
print(f"I7 cu I0 aproximata:  {rez_aprox:.8f}")
print(f"Diferenta:            {abs(rez_exact - rez_aprox):.4f}")
print("Mica eroare in I0 se amplifica masiv!")