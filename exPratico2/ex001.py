def ex01(total_cabeca, total_pe):
    pato = 0
    coelho = 0

    pato = (total_pe - total_cabeca * 2) / 2
    coelho = total_cabeca - pato

    return pato, coelho


total_cabeca = int(input("Digite a quantidade de cabeças: "))
total_pe = int(input("Digite a quantidade de pés: "))

resultado = ex01(total_cabeca, total_pe)
print(resultado)
