a, b = 0, 1
for i in range(10):
    print(a)
    a, b = b, a + b
    
# nesse caso, o a vai sempre pegar o valor do B, que em seguida será transformado em B + A