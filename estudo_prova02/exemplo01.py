def fruta(n):
    lista = ["abacaxi", "limao", "maca", "pera"]
    if n > 3:
        raise IndexError("O valor excede o número de elementos da lista")
    return lista[n]
print(fruta(4))


#escolhendo qual mensagem aparecer ao usuário informar um número excedente da lista
#através do raise ...

