from time import sleep

while True:
    nomeAtleta = input("Atleta: ")
    if nomeAtleta == "":
        break
    else:
        soma = 0
        saltos = []
        for i in range(1,6):
            salto = float(input(f"{i}º Salto: "))
            soma += salto
            saltos.append(salto)
        media = soma / 5
        
        for s in range(1):
            print("...")
            sleep(1)
            print("Calculando as médias")
            sleep(2)
            print("Quase lá")
            sleep(1)
            print("Pronto!")
            sleep(1)
            
        print(f"Atleta: {nomeAtleta}")
        
        for i in saltos:
                print(i, end=" - ")
        print()
        print(f"Média dos saltos: {media:.2f}")
        