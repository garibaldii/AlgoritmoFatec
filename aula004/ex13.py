salario_min = float(input("Digite o salário mínimo: "))
gasto_kw = float(input("Digite seu gasto mensal em kw: "))
valor_kw = salario_min / 8
gasto_kw = gasto_kw * valor_kw
desconto = gasto_kw - (gasto_kw * 0.15) 
print(f"valor do kw está = {valor_kw:.2f}")
print(f"o valor gasto ficou em = {gasto_kw:.2f}")
print(f"Com desconto de 15% fica = {desconto:.2f}")


