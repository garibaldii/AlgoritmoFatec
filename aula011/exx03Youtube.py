ls_items = []

while True:
    
    item_loja = (input("Digite os items da sua loja, para encerrar tecle enter:  "))
    if item_loja == "":
        
        break
    
    else:
        letra = list(set(item_loja))
        ls_items.append(letra)
        
print(ls_items)