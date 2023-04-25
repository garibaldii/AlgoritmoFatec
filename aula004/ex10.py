import math
numero = int(input("digite um número: "))

if numero > 0:
    
    quadrado = math.pow(numero,2)
    cubo = math.pow(numero,3)
    raiz = math.sqrt(numero)
    print(f"{numero} ao quadrado é igual a = {quadrado}")
    print(f"{numero} ao cubo é igual a = {cubo}")
    
    if raiz >= 0:
        print(f"a raiz de {numero} é {raiz}")
    else:
        print(f"não existe a raíz de {numero}")
else:
    print("Por favor, digite um número positivo ")
