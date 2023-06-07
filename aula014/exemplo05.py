arquivo = open("frutas.txt", encoding="utf-8")
texto = arquivo.read()

lista = texto.split("\n")

print(lista)
arquivo.close()
arquivo = open("frutas.txt", "a", encoding="utf-8")
while True:
    fruta = input("Digite uma fruta: ")
    if fruta == "":
        break
    elif fruta in lista:
        print("Já está cadastrado! ")
    else:
        arquivo.write(f"{fruta} \n")