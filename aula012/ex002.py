def primo(x:int):
    if x < 2:
        print(f"{x} não é primo! ")
        return
    for i in range(2,x):
        if x % i == 0:
            print(f"{x} não primo (F)")
            return
    print(f"{x} é primo (V)")
    
primo(1)
primo(10)
primo(11)