alcool = 1.7997
diesel = 0.9798
gasolina = 2.1009

escolha = input("aopa meu patrão, o que manda hoje? Temos álcool, gasolina e diesel ")
quantidade = float(input("quantos litros você vai querer? "))
if escolha.lower() == "álcool":
    valor = quantidade * alcool
    print(f"ficou R$ {valor:.2f}, campeão")
elif escolha.lower() == "gasolina":
    valor = quantidade * gasolina
    print(f"ficou R$ {valor:.2f}, campeone")
elif escolha.lower() == "diesel":
    valor = quantidade * diesel
    print(f"ficou R$ {valor:.2f}, champion")
else:
    print("Escolha uma alternativa válida!")

