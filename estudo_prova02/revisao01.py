arquivo = open("usuarios.txt", "r")
relatorio = open("relatorio.txt", "w", encoding= "utf-8")
texto = arquivo.read()

lista_1 = []
contador = 0
for linha in texto.splitlines():
    lista = linha.split(",")
    lista_1.append(lista)

dic_dados = dict(lista_1)

for chave, valor in dic_dados.items():
    dic_dados[chave] = (int(valor) / 1048576)

soma_valor = sum(dic_dados.values())

relatorio.write(f"ACME Inc.                 Uso do espaço em disco pelos usuários \n")
relatorio.write(f"--------------------------------------------------------------- \n")
relatorio.write(f"Nr.         Usuário       Espaço Utilizado    % do uso \n")
for chave, valor in dic_dados.items():
    porcentagem = (valor * 100) / soma_valor
    contador += 1
    x = f"{contador:<10} {chave:<15} {valor:>10.2f} MB {porcentagem:>10.2f} % \n"
    relatorio.write(x)

relatorio.write(f"Espaço total ocupado: {soma_valor:.2f} MB \n")
relatorio.write(f"Espaço médio ocupado: {soma_valor / len(dic_dados.values()):.2f} MB \n")
