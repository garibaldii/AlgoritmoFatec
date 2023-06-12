try:
    num = int(input("Informe o número: "))
except:
    print("Valor incorreto, digite um número normal")
else:
    print(f"boa! Você digitou {num}")
finally:
    print(f"Acabou o rolê")

#Se tudo der certo, o "else" será executado