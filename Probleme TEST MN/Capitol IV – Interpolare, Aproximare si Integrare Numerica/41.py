import numpy as np

# y' = y - t^2 + 1, y(0) = 0.5
f      = lambda t, y: y - t**2 + 1
y_exact = lambda t: (t+1)**2 - 0.5*np.exp(t)

t0, tf, h = 0, 2, 0.5
t = t0
y = 0.5

print(f"{'t':>6} {'y_euler':>12} {'y_exact':>12} {'eroare':>12}")
print(f"{t:>6.1f} {y:>12.6f} {y_exact(t):>12.6f} {abs(y-y_exact(t)):>12.2e}")

while t < tf - 1e-10:
    y = y + h * f(t, y)
    t = round(t + h, 10)
    print(f"{t:>6.1f} {y:>12.6f} {y_exact(t):>12.6f} {abs(y-y_exact(t)):>12.2e}")