def entrada():
    try:
        num = int(input("Informe um número: "))
    except:
        print("Valor Incorreto")
    else:
        print(f"Você digitou {num}")
    finally:
        print("Fim do bloco")

