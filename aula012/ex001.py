def funcao1 (x:int):
    if x % 2 == 0:
        return True
    else:
        return False
    

numero = int(input("Digite um número: "))
resultado = funcao1(numero)

print(f"{numero} é par??? -> {funcao1(numero)}")