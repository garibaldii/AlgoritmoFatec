vetorA = []
vetorB = []
for i in range(10):
    numA = int(input(F"Digite o valor para 1º, posição {i+1}:"))
    vetorA.append(numA)
    numB = int(input(F"Digite o valor para 2º, posição {i+1}:"))
    vetorB.append(numB)
vetorC = []
for i in range(10):
    vetorC.append(vetorA[i])
    vetorC.append(vetorB[i])
print(vetorC)
    
  