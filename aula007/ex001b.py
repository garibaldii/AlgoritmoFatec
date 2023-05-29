import math
e = 0
n = int(input("Digite um número inteiro positivo: "))
for i in range(n + 1):
    e += math.pow(2, i)
print(f"O valor de E= {e:.2f}")