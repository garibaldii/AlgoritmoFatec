apartamento = 0
ls_apartamento = []

while True:
    apartamento = input(f"Digite o nome do dono do apartamento {len(ls_apartamento) + 1}, para parar digite -1: ")
    
    if apartamento == "-1":
        break
    
    ls_apartamento.append((len(ls_apartamento) + 1, apartamento))

dic_apartamento = dict(ls_apartamento)

print(f"Aqui está a lista dos apartamentos: {dic_apartamento}.\n Existem {len(dic_apartamento)} apartamentos com dono!")
