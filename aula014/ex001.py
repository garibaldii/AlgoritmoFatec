with open("funcionarios.txt", "r") as arquivo:
    texto = arquivo.read()
    lista = texto.split(",")

    for i in lista:
        chave = lista[::2] #chave é par
        valor = lista[1::2]#valor é ímpar

    dicionario = dict(zip(chave,valor))
    
    for chave, valor in dicionario.items():
        dicionario[chave] = (int(valor) / 1048576)
        

    total = sum(dicionario.values())
    medio = total / len(chave)
    for chave,valor in dicionario.items():
        print(f"{chave}: {valor:.1f} MB  {((valor * 100) / total):.2f} %")
print()
print(f"Total: {total:.2f} MB")
print(f"Médio: {medio:.2f} MB")

#1 kilobyte (KB) = 1.024 bytes
#1 megabyte (MB) = 1.048.576 bytes