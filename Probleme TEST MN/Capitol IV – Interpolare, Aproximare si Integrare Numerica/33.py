def lagrange(x_nodes, y_nodes, x):
    n = len(x_nodes)
    result = 0.0
    for i in range(n):
        Li = 1.0
        for j in range(n):
            if j != i:
                Li *= (x - x_nodes[j]) / (x_nodes[i] - x_nodes[j])
        result += y_nodes[i] * Li
    return result

x_nodes = [0, 1, 2]
y_nodes = [1, 3, 7]

x_test = 1.5
rezultat = lagrange(x_nodes, y_nodes, x_test)
print(f"Puncte: {list(zip(x_nodes, y_nodes))}")
print(f"P(1.5) = {rezultat:.6f}")