fator = 1 #é necessário começar com 1 para que todos os valores não sejam multiplicados por 0, uma vez que o fator guardará os resultados loop a loop, no caso do 0, em TODOS OS LOOPS os resultados serão = 0#
x = int(input("Digite um número para saber seu fatorial: "))
if x == 0:
    print(f"o fatorial é 1")
else:
    for i in range(1, x+1):
        fator *= i
        print(i, fator) 