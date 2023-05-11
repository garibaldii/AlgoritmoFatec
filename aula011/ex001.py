ls_idade = []

for i in range(1,11):
    
    idade = int(input(f"Digite a idade nº {i}: "))
    ls_idade.append(idade)
    
    tupla_idade = tuple(ls_idade)
    
print(tupla_idade[::-1])