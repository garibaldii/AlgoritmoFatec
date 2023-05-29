idade = input("Entre com sua idade: ")

if idade.isdigit(): #verifica se todos os caracteres da string são dígitos
    idade = int(idade)
    print(idade)
else:
    print("Você digitou uma idade inválida!!")