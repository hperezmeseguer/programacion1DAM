suma = 0
contador = 0

while contador < 10:
    numeros = int(input("Introduce un número: "))

    if numeros == 999:
        break

    suma += numeros
    contador += 1

print("A suma total é:", suma)
