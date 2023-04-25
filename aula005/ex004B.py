lado_1 = int(input("Digite o lado 1: "))
lado_2 = int(input("Digite o lado 2: "))
lado_3 = int(input("Digite o lado 3: "))

if lado_1 > lado_2 + lado_3 or lado_2 > lado_1 + lado_3 or lado_3 > lado_1 + lado_2:
    print("O comprimento de cada lado de um triângulo precisa ser menor que a soma dos outros dois lados")
elif lado_1 == lado_2 == lado_3:
    print("Este triângulo é um equilátero!")
elif lado_1 == lado_2 or lado_3 == lado_1 or lado_2 == lado_3:
    print("Este triângulo é um isósceles!")
elif lado_1 != lado_2 != lado_3:
    print("Este triângulo é um escaleno!") 