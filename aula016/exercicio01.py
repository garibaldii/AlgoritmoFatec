dic_dados = {}
soma_idade = 0
soma_altura = 0
soma_peso = 0
contador = 0

def dados():
    global soma_idade, soma_altura, soma_peso, contador
    
    while True:
        sobrenome = input("Sobrenome (ou pressione Enter para sair): ")
        
        if sobrenome == "":
            break
        
        idade = int(input("Idade: "))
        altura = int(input("Altura: "))
        peso = float(input("Peso: "))

        dic_dados[sobrenome] = {
            "idade": idade,
            "altura": altura,
            "peso": peso
        }

        soma_idade += idade
        soma_altura += altura
        soma_peso += peso
        contador += 1



        

dados()

print(dic_dados)
print(f"média das idades: {soma_idade / contador}")
print(f"média das alturas: {soma_altura / contador}")
print(f"média dos pesos: {soma_peso / contador}")
print(f"{sorted(dic_dados)}")
