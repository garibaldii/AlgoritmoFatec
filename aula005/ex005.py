birth_year = int(input("Que ano vc nasceu? "))
age = 2023 - birth_year
if age > 16:
    print("vc já pode votar")
if age > 18:
    print("vc já pode dirigir")
else:
    print("você ainda não tem direitos")
