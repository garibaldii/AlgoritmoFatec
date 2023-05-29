from random import randint


n = int(input("Quantas vezes irá jogar? "))

def dado(n):
    
    for lance in range(1, n + 1):
        jogada = randint(1,6)
        jogo = print(f"Lance {lance} teve {jogada}")

resultado = dado(n)
print(resultado)