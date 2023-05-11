donos = {}
while True:
    apto = int(input("Digite o número do apto, para parar digite -1: "))
    if apto != -1:
        dono = input("Digite o nome do dono: ")
        donos.update({apto:dono})
    else:
        break
print(f" lista dos apês: {sorted(donos.items())} \n Atualmente existem {len(donos)} apartamentos comprados")