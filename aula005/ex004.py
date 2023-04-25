height = float(input("enter with your height:"))
sex = input("you are >M< or >F<?")
if sex == "m" or "M":
    weight = (72.7 * height) - 58
else:
    weight = (62.1 * height) - 44.7
print(f"your ideal weight is {weight:.2f}kg")