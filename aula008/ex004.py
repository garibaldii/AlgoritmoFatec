frase = input("Digite uma frase: ")
vogal = 0
for i in frase:
    if i in "aeiouAEIOU":
        vogal += 1
print(f"Existem {vogal} vogais nesta frase.")

#para percorrer por strings usa-se o "in" e interáveis usa-se o "range". 

