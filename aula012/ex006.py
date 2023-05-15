def horario (horaSegundos:int, minutoSegundos:int, segundos:int):
    horaSegundos *= 3600
    minutoSegundos *= 60
    horario = horaSegundos + minutoSegundos + segundos
    return horario

print(f" o valor de 4h, 58min e 30seg é = {horario (4,58,30)} segundos")
