"""Elaborar um algoritmo que imprime na tela os
dez primeiros múltiplos de um número
inteiro qualquer fornecido pelo usuário (lido).
No final, imprima também a soma destes dez
números.
Exemplo da saída:
Valor lido: 3
Lista de Múltiplos: 3 6 9 12 15 18 21 24 27 30
Soma = 165 """

num = int(input())
multiplos = []
contador = 1

for i in range(1,11):
    multiplos.append(i * num)
print(num)
print(multiplos)
print(sum(multiplos))
        