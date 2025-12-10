n = int(input("Cuánto miden la base y la altura?: "))

for i in range(1, n + 1):
    espacios = " " * (n - i)
    estrellas = "* " * i
    print(espacios + estrellas)
