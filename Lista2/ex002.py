from time import sleep

print("Qual o melhor Sistema Operacional para uso em servidores?")
print()
print("As possíveis respostas são: ")
print()
print("1- Windows Server")
print("2- Unix")
print("3- Linux")
print("4- Netware")
print("5- Mac OS")
print("6- Outro")

modelo = ["Windows Server", "Unix", "Linux", "Netware", "Mac OS", "Outro"]
sistemasOp = [0] * 6
votos_totais = 0

while True:
    escolha = int(input("Digite o número: "))
    if escolha == 0:
        print()        
        print("Sistema Operacional    Votos    %")
        print("-------------------    -----    ---")
        for i, voto in enumerate(sistemasOp):
            porcentagem = (voto / votos_totais) * 100
            print(f"{modelo[i]:<25} {voto:<7} {porcentagem:<.1f}%")
        print("-------------------    -----    ---")
        break
    
    elif 1<= escolha <= 6:
        sistemasOp[escolha-1] += 1
        votos_totais +=1
        
    elif escolha > 6 or escolha < 0:
        print("Digite uma opção válida!")
        for i in range(1):
            sleep(1.3)
            print("--------------")