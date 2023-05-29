from funcoes import rola_dado
from time import sleep

print("---------------")
print("Jogo de dados")
print("---------------")

placar_user = 0
placar_pc = 0

while True:
    escolha = input("Pressione >Enter< para jogar: ")
    if escolha == "":
        usuario = rola_dado()
    print(f"Você tirou {usuario}!")
    print(f"agora é a vez do pc!")
    for i in range(2):
        sleep(1)
        print(".")
        pc = rola_dado()
    print(f"O PC tirou {pc}!")
    if pc > usuario:
        print("Pc ganhou!")
        placar_pc += 1
    elif pc == usuario:
        print("Empate!")
    else:
        print("Você ganhou!")
        placar_user += 1
    
    jogar_novamente = input("Você deseja jogar novamente? >s< ou >n<: ")
    if jogar_novamente == "n":
        print(f"O placar ficou: USER = {placar_user} X {placar_pc} = PC")
        break