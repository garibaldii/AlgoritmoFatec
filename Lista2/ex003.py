num = int(input("Digite um num: "))
num_invertido = 0

while num > 0:
    resto = num % 10 #separar o último digito(resto)
    num_invertido = (num_invertido * 10) + resto #atribuir o valor para o num_invertido
    num = num // 10 #separar o último dígito para seguir a sentido próximo

print(num_invertido)