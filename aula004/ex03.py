ano_atual = 2023
nascimento = int(input("Digite o ano que você nasceu: "))

idade_ano = ano_atual - nascimento
idade_mes = idade_ano * 12
idade_dia = idade_ano * 365
idade_semana = idade_dia / 52

print(f"você tem {idade_ano} anos ou {idade_mes} mêses ou {idade_dia} dias ou {idade_semana} semanas")

