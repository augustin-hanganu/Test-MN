from decimal import Decimal, getcontext
getcontext().prec = 50

x_float   = 1/3
ok_float  = (x_float * 3 == 1)

x_dec     = Decimal(1) / Decimal(3)
ok_dec    = (x_dec * 3 == 1)

print(f"float:   1/3 = {x_float:.20f}")
print(f"(1/3)*3 == 1 ? {ok_float}")
print(f"\nDecimal: 1/3 = {x_dec}")
print(f"(1/3)*3 == 1 ? {ok_dec}")