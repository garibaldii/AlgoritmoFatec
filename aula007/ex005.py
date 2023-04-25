soma_p = 0
soma_a = 0
imc_max = 0
imc_min = 100

for i in range(1, 21):
    peso = float(input(f"Digite o peso {i}: "))
    altura = float(input(f"Digite a altura {i}: "))
    imc = (peso/ (altura ** 2))
    soma_p += peso
    soma_a += altura
    
    if imc > imc_max:
        imc_max = imc

    if imc < imc_min:
        imc_min = imc

media_p = soma_p / 20
media_a = soma_a / 20

print(f"o peso médio é {soma_p}")
print(f"a altura média é {soma_a}")
print(f"o maior imc é {imc_max}")
print(f"o menor imc é {imc_min}")
