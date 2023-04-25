soma_idades = 0
qtd_pessoas =0

while True:
    idades = int(input("Digite as idades para se obter a média, entre com 0 para encerrar: "))
    if idades == 0:
        break
    soma_idades += idades
    qtd_pessoas += 1
    
if qtd_pessoas > 0:
    media = soma_idades / qtd_pessoas
    print(f" a soma das {qtd_pessoas} idades é igual a {media:.2f}")
else:
    print("digite pelo uma idade para poder entrar com o 0! ")
    
    
        