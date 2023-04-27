frase = ""
for i in range(1,21): 
    palavra = input("Digite uma palavra de no máximo 10 caracteres: ")[:10]
    frase += palavra + " "
    if len(palavra) > 10:
        print("você digitou uma palavra maior que 10 caracteres :(")
print(frase[::-1])
