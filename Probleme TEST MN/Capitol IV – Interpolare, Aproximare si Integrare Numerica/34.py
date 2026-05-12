import numpy as np

def divided_diff(x, y):
    n = len(x)
    table = np.zeros((n, n))
    table[:, 0] = y
    for j in range(1, n):
        for i in range(n - j):
            table[i][j] = (table[i+1][j-1] - table[i][j-1]) / (x[i+j] - x[i])
    return table

def newton_dd(x_nodes, table, x):
    n = len(x_nodes)
    result = table[0][0]
    prod = 1.0
    for k in range(1, n):
        prod *= (x - x_nodes[k-1])
        result += table[0][k] * prod
    return result

x_nodes = [0, 1, 2]
y_nodes = [1, 3, 7]
table   = divided_diff(x_nodes, y_nodes)

print("Tabel diferente divizate:")
print(table)
print(f"\nP(1.5) = {newton_dd(x_nodes, table, 1.5):.6f}")