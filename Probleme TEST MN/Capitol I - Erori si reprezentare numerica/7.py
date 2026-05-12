x_real = 13;   x_calc = 14
y_real = 1386; y_calc = 1387

def erori(real, calc):
    abs_err = abs(real - calc)
    rel_err = abs_err / abs(real)
    return abs_err, rel_err

ea_x, er_x = erori(x_real, x_calc)
ea_y, er_y = erori(y_real, y_calc)

print(f"x: eroare absoluta = {ea_x}, eroare relativa = {er_x:.4f} ({er_x*100:.2f}%)")
print(f"y: eroare absoluta = {ea_y}, eroare relativa = {er_y:.6f} ({er_y*100:.4f}%)")
print("\nConcluzie: Aceeasi eroare absoluta (1), dar eroarea relativa")
print("este mult mai mica pentru y → aproximarea lui y este mai buna!")