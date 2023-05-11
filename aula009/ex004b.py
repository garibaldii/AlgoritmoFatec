
frase = ""
for i in range(1, 21):
    palavra = input("Digite uma palavra para fazer uma frase: ")[:10]
    frase += palavra    
print(frase[::-1])