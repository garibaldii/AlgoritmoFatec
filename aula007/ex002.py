while True:
    base = int(input("Digite a base: "))
    altura = int(input("Digite a altura: "))
    if base > 0 and altura > 0:
        area = ((base * altura) /2)
        print(f"A área do triângulo é igual a {area:.2f}")
    else:
        print(f"Digite um valor válido, reiniciando o ciclo...")