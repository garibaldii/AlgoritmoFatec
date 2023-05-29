nome1 = input("Digite seu 1ª nome:")
nome2 = input("Digite seu 2ª nome:")
nome3 = input("Digite seu 3ª nome:")

lista_nome = [nome1, nome2, nome3]
nome_completo = " ".join(lista_nome)
print(nome_completo)

nome_cripto = ''
for indice in range(0, len(nome_completo)):
    nome_cripto += chr(ord(nome_completo[indice])+1)

print(f"Nome Cripto: {nome_cripto}")