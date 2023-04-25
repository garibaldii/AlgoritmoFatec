ano_atual = int(input("digite o ano de hoje: "))
mes_atual = int(input("digite o mês atual: "))
dia_atual = int(input("digite o dia atual: "))

nasc_ano = int(input("digite o ano de nascimento:"))
nasc_mes = int(input("digite o mes de nascimento:"))
nasc_dia = int(input("digite o dia de nascimento:"))

idade_ano = ano_atual - nasc_ano
if nasc_mes > mes_atual:
    idade_ano += 1

idade_mes = (mes_atual - nasc_mes)
if idade_mes < 0:
    idade_mes += 12
    idade_ano = -1

idade_dia = (dia_atual - nasc_dia)
if idade_dia < 0:
    idade_dia += 30
    idade_mes += -1

print(f"você tem {idade_ano} anos ,{idade_mes} meses e {idade_dia} dias")
    





