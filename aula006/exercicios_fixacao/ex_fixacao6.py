acerto = int(input("Quantas questões você acertou? "))
if acerto > 0 and acerto <= 49:
    print("vc tirou a nota D")
elif acerto > 50 and acerto <= 69:
    print("vc tirou a nota C")
elif acerto > 700 and acerto <= 80:
    print("vc tirou a nota B")
elif acerto > 90 and acerto <= 100:
    print("vc tirou a nota A")
else:
    print("vc foi desclassificado de tanta burrice")