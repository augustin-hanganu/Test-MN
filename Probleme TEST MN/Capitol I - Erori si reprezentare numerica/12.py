import struct

val = 0.1
# obtinem bitii IEEE 754
bits = struct.pack('d', val)
b    = int.from_bytes(bits, 'little')
binar = f"{b:064b}"

print(f"0.1 in baza 2 (IEEE 754):")
print(f"  Semn:     {binar[0]}")
print(f"  Exponent: {binar[1:12]}")
print(f"  Mantisa:  {binar[12:]}")
print(f"\nValoare stocata: {val:.20f}")
print(f"Valoare exacta:  0.10000000000000000000")
print(f"Eroare:          {abs(val - 0.1):.2e}")