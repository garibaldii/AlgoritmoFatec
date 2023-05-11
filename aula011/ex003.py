from random import randint  

lista1 = [randint(1,11) for i in range (10)] 
lista2 = [randint(1,11) for i in range (10)] 

print(f"esta é a lista 1: {lista1}")
print(f"esta é a lista 2: {lista2}")

lista3 = lista1 + lista2

print(f"Esta é a lista 3, resultado da união da lista 1 com a lista 2: {lista3}")