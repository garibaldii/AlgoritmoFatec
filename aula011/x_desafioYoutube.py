dados = {}
soma_idade = 0
soma_calcado = 0

for i in range(1,6):
    
    nome = input(f"Digite o nome da pessoa {i}: ")
    idade = int(input(f"Digite a idade da pessoa {i}: "))
    calcado = int(input(f"Digite o número de calçado da pessoa {i}: "))
    
    soma_idade += idade
    soma_calcado += calcado
    dados.update({nome: (idade, calcado)})
    
print(f"a média das idades é {soma_idade / 5} e dos calçados é {int(soma_calcado / 5)}")

print(f"aqui está a lista em ordem alfabética: {sorted(dados.items())}")
