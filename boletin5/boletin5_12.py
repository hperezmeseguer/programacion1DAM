sueldos = [1000, 2000, 1749, 1200, 800, 2050]

entre1000_1750 = 0
menos1000 = 0
for conteo in sueldos:
    if conteo >= 1000 and conteo <= 1750:
        entre1000_1750 += 1

    elif conteo < 1000:
        menos1000 += 1

    elif conteo < 0:
        break

porcentaje = menos1000/len(sueldos)*100

print(f"Hay {entre1000_1750} personas que cobran entre 1000 y 1750 euros")
print(f"El porcentaje de trabajadores que cobran menos de 1000 euros es {porcentaje:.2f}%")
