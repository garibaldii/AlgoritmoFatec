try:
    with open("frutas.txt", "x", encoding= "utf-8") as arquivo:
        while True:
            fruta = input("Fruta: ")
            if fruta == "sair":
                break
            else:
                arquivo.write(fruta)
                arquivo.write("\n")
except:
    print("Arquivo já existente")
    
    
    
    
    
    
    
    
    
    for j in lista_inicial:
    lista_final += j.split(",")

for m in range(1, len(lista_final), 2):
    lista_consumo.append(lista_final[m])
print(lista_consumo)