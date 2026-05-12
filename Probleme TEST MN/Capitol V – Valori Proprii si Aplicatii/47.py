import numpy as np

# g1(x,y) = sqrt(4 - y^2)  → converge
# g2(x,y) = 1 - e^x        → nu converge

def iter_g1(v):
    x, y = v
    return np.array([np.sqrt(max(4 - y**2, 0)), y])

def iter_g2(v):
    x, y = v
    return np.array([x, 1 - np.exp(x)])

v0 = np.array([1.0, 1.5])

print("g1 (converge):")
v = v0.copy()
for i in range(10):
    v_nou = iter_g1(v)
    print(f"  iter {i}: {v_nou}, |Δ|={np.linalg.norm(v_nou-v):.4f}")
    if np.linalg.norm(v_nou - v) < 1e-6: break
    v = v_nou

print("\ng2 (diverge):")
v = v0.copy()
for i in range(10):
    v_nou = iter_g2(v)
    print(f"  iter {i}: {v_nou}, |Δ|={np.linalg.norm(v_nou-v):.4f}")
    if np.linalg.norm(v_nou - v) > 100: print("  DIVERGE!"); break
    v = v_nou