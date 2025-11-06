from boletin2.boletin2_1 import area_triangulo

figura = input("De qué figura quieres calcular el área: Triángulo, Cuadrado o Círculo?:")

if figura == "Triángulo":
    base = float(input("Cuánto mide la base?:"))
    altura = float(input("Cuánta altura tiene?:"))
    area_triangulo = float((base * altura)/2)
    print(area_triangulo)

elif figura == "Cuadrado":
    lado = float(input("Cuánto mide el lado?:"))
    area_cuadrado = lado * lado
    print(area_cuadrado)

elif figura == "Círculo":
    pi = float(3.14)
    radio = float(input("Cuánto mide el radio?:"))
    area_circulo = float(pi * (radio * radio))
    print(area_circulo)

else:
    print("Opción incorrecta")

