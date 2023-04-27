lista = []
for i in range(1,11):
    num = int(input(f"Digite um número para entrar na lista na posição {i}: "))
    lista.append(num)

maior_valor = max(lista)
posicao_mv = lista.index(maior_valor) + 1

print(f"o maior valor é {maior_valor} e sua posição é {posicao_mv}") 
