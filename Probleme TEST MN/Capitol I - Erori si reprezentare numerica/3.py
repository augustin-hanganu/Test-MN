numere = [0.2146, 3.175, 15.421, 176.86]

crescator  = sum(sorted(numere))
descrescator = sum(sorted(numere, reverse=True))

print(f"Crescator:    {crescator:.4f}")
print(f"Descrescator: {descrescator:.4f}")
print(f"Diferenta:    {abs(crescator - descrescator):.2e}")


x1 = 0.2146
x2 = 3.175
x3 = 15.421
x4 = 176.86

print(f"Crescator1: {0.2146 + 3.175 + 15.421 + 176.86:.10f}")
print(f"Descrescator1: {176.86 + 15.421 + 3.175 + 0.2146:.10f}")
