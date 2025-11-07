unidades = ["", "uno", "dos", "tres", "cuatro", "cinco", "seis", "siete", "ocho", "nueve"]
decenas = ["", "diez", "veinti", "treinta", "cuarenta", "cincuenta", "sesenta", "setenta", "ochenta", "noventa"]
otros = ["once", "doce", "trece", "catorce", "quince", "dieciseis", "diecisiete", "dieciocho", "diecinueve"]

n = int(input("Introduce un número entre 1 y 99: "))

if n < 1 or n > 99:
    print("El número debe estar entre 1 y 99.")
else:
    if n < 10:
        print(unidades[n])

    elif n == 10:
        print("diez")

    elif 10 < n < 20:
        print(otros[n-11])

    elif n == 20:
        print("veinte")

    elif 20 < n < 30:
        print(decenas[2] + unidades[n % 10 - 1])

    else:
        d = n // 10
        u = n % 10
        if u == 0:
            print(decenas[d])
        else:
            print(decenas[d] + " y " + unidades[u - 1])

