soma = 0
while True:
    m = int(input("Digite um valor inteiro e positivo para m: "))
    n = int(input("Digite um valor inteiro e positivo para n: "))
    if m > n:  
            
        for i in range(n, m + 1, 2):
            soma += i
            print(f"a soma dos valores entre {n} e {m} é igual a {soma}")
        break
    else:
        print(f"erro, {m} precisa ser maior que {n}")
