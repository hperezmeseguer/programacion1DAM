while True:
    numero = int(input("De que número quieres ver su tabla?:"))

    if numero == 0:
        break

    for i in range(1,11):
         print(f"{numero} x {i} = {numero * i}")