import numpy as np

val32 = np.float32(1/3)
val64 = np.float64(1/3)

print(f"float32: {val32:.20f}")
print(f"float64: {val64:.20f}")
print(f"Exact:   {1/3}")