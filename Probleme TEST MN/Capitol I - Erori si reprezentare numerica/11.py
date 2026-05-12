from decimal import Decimal, getcontext
getcontext().prec = 70

val_float   = 2.0 ** 200
val_decimal = Decimal(2) ** 200
val_exact   = 2 ** 200  # Python int exact

print(f"float64:  {val_float:.6e}")
print(f"Decimal:  {val_decimal}")
print(f"Exact:    {val_exact}")
print(f"\nEroare float: {abs(val_float - val_exact):.6e}")