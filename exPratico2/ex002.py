lista_primo = []
def primo(num):
    contador = 0
    if num < 2:
            return False
    for i in range(1,num+1):
        if num % i == 0:
            contador += 1
        if contador > 2:
            return False
    return True

def primo2(y):
    lista_primo = []
    for i in range(1, y + 1):
          if primo(i):
               lista_primo.append(i)
    return sum(lista_primo)
    

print(primo2(85))


