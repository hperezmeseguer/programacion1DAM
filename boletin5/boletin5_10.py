base = int(input("Cuánto mide la base?:"))
altura = int(input("Cuánto hay de altura?:"))


for comprobacion in range(base, altura):
    area = base * altura
    if comprobacion < 0:
        break
    else:
        print(f"El área es de:{area}")