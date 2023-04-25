#falta fixar o preço do dolar de alguma forma# 
dolar = 5
dolar_ponto = 1.5

ponto = int(input("Quantos pontos você quer simular? "))
calculo = (ponto/ dolar_ponto) * dolar
print(f"Você precisa gastar R${calculo:.2f}")


