compra = float(input("Total da compra = "))
if compra <1000:
    valor = compra - (compra * 10/100)
    print(f"com desconto = {valor}")
elif (compra >= 1001) and (compra <=5000):
    valor = compra - (compra * 20/100)
    print(f"com desconto = {valor}")
elif compra > 5000:
    valor = compra - (compra * 30/100)
    print(f"com desconto = {valor}")