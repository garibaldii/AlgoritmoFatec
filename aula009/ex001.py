print("Criando uma lista com 10 elementos!")

lista = []

for i in range(10):
    num = int(input("Digite um valor: "))
    lista.append(num)
print(f" Sua lista ao contrário -> {lista [::-1]}")
    