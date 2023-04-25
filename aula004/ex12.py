altura_degrau = int(input("Digite a altura dos degrais em cm: "))
altura_degrau = altura_degrau / 100
if altura_degrau > 0:
        escada = float(input("Digite a altura da escada em m: "))
        qtd_degrau = escada // altura_degrau
        extra = (escada % altura_degrau)*100
        print(f" precisa de {qtd_degrau} degraus de {altura_degrau:.2f} cm e mais {extra:.2f} cm extras")
else:
        print("Insira um valor válido!")
