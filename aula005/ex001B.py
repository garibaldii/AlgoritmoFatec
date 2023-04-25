a = int(input("digite um número: "))
b = int(input("digite outro número: "))

print(f"sua média é {(a + b) / 2}")

if a > b:
    diferenca = a - b
    print(f"sua diferença é {diferenca}")
else:
    diferenca = b - a
    print(f"sua diferença é {diferenca}")
    
print(f"seu produto é {a * b}")
print(f"sua divisão é {a / b}")
