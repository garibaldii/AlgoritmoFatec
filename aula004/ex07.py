
deposito = 0
while deposito <= 0:
    deposito = float(input("Insira um valor para depositar:"))
    if deposito > 0:
        juros = input("você quer 1%(2023), 2%(2024) ou 3%(2025)?")
        if juros == "1%":
            resultado = deposito * 1.001
            print(f"seu rendimento será de R${resultado}")
        elif juros == "2%":
            resultado = deposito * 1.002
            print(f"seu rendimento será de R${resultado}")
        elif juros == "3%":
            resultado = deposito * 1.003
            print(f"seu rendimento será de R${resultado}")
    else:
        print("Digite um número válido")
