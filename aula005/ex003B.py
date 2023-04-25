p_liquido = float(input("Digite o preço líquido do produto: "))
cod_origem = int(input("Digite o código de origem: "))
regiao = 0
if cod_origem == 1:
    regiao = "Sul"
    imposto = (11/100) + 1
    p_final = imposto * p_liquido
    print(regiao)
    print(f"preço final = {p_final:.2f}")
    
elif cod_origem == 2:
    regiao = "Norte"
    imposto = (13/100) + 1
    p_final = imposto * p_liquido
    print(regiao)
    print(f"preço final = {p_final:.2f}")
    
elif cod_origem == 3:
    regiao = "Nordeste"
    imposto = (9/100) + 1
    p_final = imposto * p_liquido
    print(regiao)
    print(f"preço final = {p_final:.2f}")
    
elif cod_origem == 4:
    regiao = "Centro-Oeste"
    imposto = (12/100) + 1
    p_final = imposto * p_liquido
    print(regiao)
    print(f"preço final = {p_final:.2f}")
    
elif cod_origem == 5:
    regiao = "Sudeste"
    imposto = (18/100) + 1
    p_final = imposto * p_liquido
    print(regiao)
    print(f"preço final = {p_final:.2f}")
else:
    print("Digite um código válido")