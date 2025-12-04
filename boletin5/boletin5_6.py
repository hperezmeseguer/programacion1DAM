valores = int(input("Qué cantidad de valores quieres calcular: "))

for i in range(1, valores + 1):
    numero = int(input("Introduce el número que quieras:"))

    factorial = 1
    for j in range(1, numero + 1):
        factorial = factorial * j

    print(f"El factorial de {numero} es {factorial}")
