arquivo = open("texto.txt", encoding="utf-8")
texto = arquivo.read()
print(texto)


print(texto.split(" "))
for i in texto:
    print(i)