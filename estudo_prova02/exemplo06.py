arquivo = open("texto.txt", "r")
lista = []
texto = arquivo.read()
for linha in texto.splitlines():#criar um interável com todas as linhas, separar cada linha por \n 
    lista.append(linha)
print(lista)
arquivo.close()