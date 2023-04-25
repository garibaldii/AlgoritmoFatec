data = input("Digite uma data no formato dd/mm/aaaa: ")
dia = data[0:2]
mes = data[3:5]
ano = data[6:10]

ls_eua = [ano, mes, dia]

ano_eua = "".join(ls_eua)
print(ano_eua)
