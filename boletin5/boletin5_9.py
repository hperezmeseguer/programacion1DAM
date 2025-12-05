numeros = (10, -2, 3, 4, 0, 0, 2, -3, -5, 11)
positivos = 0
negativos = 0
ceros = 0

for i in numeros:
    if i > 0:
        positivos += 1

    elif i < 0:
        negativos += 1
    else:
        ceros += 1

print("Positivos:", positivos)
print("Negativos:", negativos)
print("Ceros:", ceros)
