idade = 0
lista_idade = []
while idade != -1:
    idade = int(input("Digite várias idades, se quiser parar digite -1: "))
    if idade == -1:
        break
    lista_idade += [idade] #poderia usar o lita_idade.append(idade) para adicionar os inteiros na lista também
tupla_idade = tuple(lista_idade)
qtd_idade = len(tupla_idade)
media = sum(tupla_idade) / qtd_idade
print(tupla_idade)
print(f"Você digitou {qtd_idade} idades e a média é {media:.2f}!")
    