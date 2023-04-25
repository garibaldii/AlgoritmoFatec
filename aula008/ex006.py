palavra = input("Digite uma palavra: ")
print(palavra)

palavra_contrario = palavra[::-1]
print(palavra_contrario)

if palavra == palavra_contrario:
    print("essa palavra é um Palíndromo")
else:
    print("esta palavra não é um Palíndromo")