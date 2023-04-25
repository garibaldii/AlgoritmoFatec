num = int(input("Digite um número inteiro maior que 1: "))

if num <= 1:
    print("O número deve ser maior que 1.")
else:
    div_contador = 0
    
    # Loop para verificar se o número é divisível por algum número entre 2 e a sua raiz quadrada
    for i in range(2, int(num**0.5)+1):
        if num % i == 0:
            div_contador += 1
            break
            
    if div_contador > 0:
        print(f"{num} não é um número primo.")
    else:
        print(f"{num} é um número primo.")
