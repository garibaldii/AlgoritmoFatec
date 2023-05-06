from random import randint
frequencia = [0] * 6
simulacao = []
for i in range(6000):
    jogada = randint(1,6)
    simulacao.append(jogada)
print(simulacao)

for i in range(6000): #a expressão jogada - 1 é usada como índice para acessar o elemento correto na lista frequencia. Como a lista começa na posição 0, a variável jogada que pode ser 1, 2, 3, 4, 5 ou 6 é subtraída de 1 para obter o índice correto da lista.
    frequencia[simulacao[i] - 1] += 1 
print(frequencia)
    
    
