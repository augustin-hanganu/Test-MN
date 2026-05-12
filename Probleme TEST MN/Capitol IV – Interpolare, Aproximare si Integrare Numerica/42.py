import numpy as np

# y' = y - t^2 + 1, y(0) = 0.5
f       = lambda t, y: y - t**2 + 1
y_exact = lambda t: (t+1)**2 - 0.5*np.exp(t)

t0, tf, h = 0, 2, 0.5
t = t0
y = 0.5

print(f"{'t':>6} {'y_rk4':>12} {'y_exact':>12} {'eroare':>12}")
print(f"{t:>6.1f} {y:>12.6f} {y_exact(t):>12.6f} {abs(y-y_exact(t)):>12.2e}")

while t < tf - 1e-10:
    k1 = f(t,       y)
    k2 = f(t + h/2, y + h/2 * k1)
    k3 = f(t + h/2, y + h/2 * k2)
    k4 = f(t + h,   y + h   * k3)
    y  = y + h/6 * (k1 + 2*k2 + 2*k3 + k4)
    t  = round(t + h, 10)
    print(f"{t:>6.1f} {y:>12.6f} {y_exact(t):>12.6f} {abs(y-y_exact(t)):>12.2e}")

print("\nRK4 este mult mai precis decat Euler!")