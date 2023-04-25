
nota1 = float(input("Digite a 1a nota: "))
nota2 = float(input("Digite a 2a nota: "))
nota3 = float(input("Digite a 3a nota: "))
while (nota1 < 0 or nota1 > 10 or nota2 < 0 or nota2 > 10 or nota3 < 0 or nota3 > 10):
    print("Digite um valor válido para as notas")
    nota1 = float(input("Digite a 1a nota: "))
    nota2 = float(input("Digite a 2a nota: "))
    nota3 = float(input("Digite a 3a nota: "))
    
media = (nota1 + nota2 + nota3) / 3

if (media >= 7) and (10 >= media):
    print("aprovado")
elif (media >= 3) and (7 > media):
    print("exame")
elif (media == 0) and (3 > media):
    print("reprovado")