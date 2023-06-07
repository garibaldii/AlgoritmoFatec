ls_carros1 = ["Civic", "Pajero", "Ecosport", "Range Rover", "Fiesta"]
ls_carros_consumo = [7, 10, 9, 8, 14]

dic_dados = dict(zip(ls_carros1, ls_carros_consumo))

mais_economico = max(dic_dados.values())

for carro, consumo in dic_dados.items():
    dic_dados[carro] = round((1000 / consumo) * 5.65)

print(dic_dados)
print(mais_economico)