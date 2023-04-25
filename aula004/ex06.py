print("Você ganhou um aumento salarial!!")

salario = int(input("Digite seu salário: "))
escolha = input("Você ganhou em valor ou porcentagem? ")
x = escolha.lower()
if x == ("porcentagem"):
    aumento = int(input("Digite quantos % você ganhou de aumento: "))
    novo_salario = (aumento/100 + 1) * salario
    
else:
    aumento = int(input("Digite qual valor você ganhou: "))
    novo_salario = salario + aumento
    
print(f"Seu novo salário é: {novo_salario:.2F} ")