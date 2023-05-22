def primo(x:int):
    if x < 2:
        return False
    for i in range(2,x):
        if x % i == 0:
            return False
    return True

contador = 0
num_primo = 2

while contador < 50:
    if primo(num_primo):
        print(num_primo, end= "-")
        contador += 1    
    num_primo += 1