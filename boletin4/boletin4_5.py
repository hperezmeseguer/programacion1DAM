dni = int(input("dime un dni:"))
letras = ["T", "R", "W", "A", "G", "M", "Y", "F", "P", "D", "X", "B", "N", "J", "Z", "S", "Q", "V", "H", "L", "C", "K", "E"]

letra_dni = letras[dni % 23]
print(f"EL DNI es: {dni}{letra_dni}")