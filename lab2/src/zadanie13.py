"""Wyzwól następujący kod, wyświetl K, L, M i N. Wyjaśnij w jaki sposób konkatenacja 
zachowuje się inaczej od przypisania rozszerzonego."""

K = [1, 2]
L = K
K = K + [3, 4]
M = [1, 2]
N = M
M += [3, 4]

print(K)
print(L)
print(M)
print(N)