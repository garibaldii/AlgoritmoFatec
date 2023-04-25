idade = int(input("Digite sua idade, atleta!:"))
if idade >= 5 and idade <= 7:
    print("INFANTIL")
elif idade >= 8 and idade <= 10:
    print("JUVENIL")
elif idade >=11 and idade <=15:
    print("ADOLESCENTE")
elif idade >= 16 and idade <= 30:
    print("ADULTO")
elif idade > 30:
    print("SÊNIOR")
else:
    print("vc não tem idade para nadar!")
    