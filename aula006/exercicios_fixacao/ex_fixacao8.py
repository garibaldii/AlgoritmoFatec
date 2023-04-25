import math
largura = float(input("Digite a largura do cômodo: "))
comprimento = float(input("Digite o comprimento do cômodo: "))
pe_direito = 2.8
gasto =  (comprimento * pe_direito) + ((largura * pe_direito) - 1.70 )
print(gasto)
tamanho_lata = (input("Sua lata é de >1L<, >3L< ou >18L<?"))
if tamanho_lata == "1L":
    qtd_lata1 = int(math.ceil(gasto / 3))
    print(f"você irá precisar de {qtd_lata1} latas de tinta!")
elif tamanho_lata == "3L":
    qtd_lata1 = int(math.ceil(gasto / 9))
    print(f"você irá precisar de {qtd_lata1} latas de tinta!")
elif tamanho_lata == "18L":
    qtd_lata1 = int(math.ceil(gasto / 54))
    print(f"você irá precisar de {qtd_lata1} latas de tinta!")

     