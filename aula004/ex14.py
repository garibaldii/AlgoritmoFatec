horario = float(input("Digite um horário: "))
hora = int(horario)
minutos = (horario - hora) * 100 #multiplicado por 100 para transformar horar em minutos, interar ex. 0.3 = 30 min
total_minutos = hora * 60 + minutos
print(f"em minutos = {total_minutos}") 