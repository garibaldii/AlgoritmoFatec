#fiz esse exercício de três formas. forma1 = "ex02AYoutube.py", forma2 = "ex02BYoutube.py" e forma3 = "ex02CYoutube.py"
apartamento = 0
ls_apartamento = []
for i in range(1,1000):
    apartamento = input(f"Digite o nome do dono do apartamento {i}, para parar digite -1: ")
    if apartamento == "-1":
        break
    else:
        ls_apartamento += [(i, apartamento)]
        dic_apartamento = dict(ls_apartamento)

print(f"Aqui está a lista dos apartamentos: {dic_apartamento}.\n Existem {len(dic_apartamento)} apartamentos com dono!")
    