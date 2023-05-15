import math

def mdc(x:int, y:int): #A função math.gcd() utiliza um algoritmo eficiente para calcular o MDC. Ela implementa o algoritmo de Euclides, que consiste em sucessivas divisões e trocas de valores até que o resto da divisão seja igual a zero.
    return math.gcd(x,y) 

resultado = mdc(20,30)
print(resultado) 