ls_ip_aprovado = []
ls_ip_negado = []
end_ip = None

while end_ip != "":
    
    end_ip = input("Digite um endereço ip: ")

    ip_separado = end_ip.split(".") #[1.2."3"]
    ip_formatado = list(map(int, ip_separado)) #transforma o ip separado de strings para int

    if len(ip_formatado) == 4:
        ip_valido = True
        for i in ip_formatado:
            if i > 255 or i < 0:
                ip_valido = False
                break

        if ip_valido:
            ls_ip_aprovado.append(ip_formatado)
            
        else:
            ls_ip_negado.append(ip_formatado)

    else:
        ls_ip_negado.append(ip_formatado)
            

    print("[Endereços Válidos: ]")
    for ip in ls_ip_aprovado:
        print(".".join(map(str,ip)))
        
    print()
    
    print("[Endereços Inválidos: ]")
    for ip in ls_ip_negado:
        print(".".join(map(str,ip)))