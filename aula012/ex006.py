def horario(hora):
    horaSegundos = int(hora[0]) * 3600
    minutosSegundos = int(hora[1]) * 60
    segundos = int(hora[2])
    return (horaSegundos + minutosSegundos + segundos)

hora = input("Digite o horário separado por dois pontos: ")
hora_split = hora.split(":")
print(f" o seu horário em segundos é igual a {horario(hora_split)}")
print(hora_split)
