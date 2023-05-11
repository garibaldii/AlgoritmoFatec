ls_dados = []

for i in range(1,3):
    sobrenome = input(f"Digite o sobrenome da pessoa {i}: ")
    idade = int(input(f"Digite a idade da pessoa {i}: "))
    
    ls_dados.append((sobrenome, idade))
    
print(ls_dados)
dic_dados = dict(ls_dados)

maior_idade = max(dic_dados.values())
sobrenome_maior_idade = max(dic_dados, key=dic_dados.get) 
#key=meu_dict.get diz ao max() para usar o valor correspondente a cada chave como o valor a ser comparado para encontrar o maior valor.o Python irá iterar sobre as chaves 'a', 'b' e 'c' e chamar ls_dados.get() para cada chave.

print(f"{dic_dados}\n A maior idade é do {sobrenome_maior_idade}, ele tem {maior_idade} anos ")