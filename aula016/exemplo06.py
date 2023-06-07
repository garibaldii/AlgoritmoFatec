def entrada():
    try:
        num = int(input("Informe um número: "))
    except:
        return None
    else:
        return num
    finally:
        print("Fim do bloco")

a = entrada()
print(a)