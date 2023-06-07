with open("times.txt", "w") as arquivo:
    while True:
        fruta = input("Digite um texto: ")
        if fruta == "sair":
            break
        else:
            arquivo.write(fruta)
            arquivo.write("\n")

#função do with é fornecer um contexto de execução controlado para recursos externos e garantir que esses recursos sejam liberados corretamente ao final do bloco with, mesmo em caso de erros. 

#with == enter() e exit() implementados adequadamente!!!!!!