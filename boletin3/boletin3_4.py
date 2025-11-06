nombre1 = "Jose"
nombre2 = "Ana"
pesoJose = float(input("Cuánto pesa Jose?:"))
pesoAna = float(input("Cuánto pesa Ana?:"))

if pesoJose > pesoAna:
    diferencia_peso = pesoJose - pesoAna
    print(f"{nombre1} pesa {diferencia_peso} kilos más que {nombre2}")

elif pesoAna > pesoJose:
    diferencia_peso = pesoAna - pesoJose
    print(f"{nombre2} pesa {diferencia_peso} kilos más que {nombre1}")

else:
    print("Pesan lo mismo")