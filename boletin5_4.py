num1 = int(input("Dime un numero:"))
num2 = int(input("Dime un numero:"))

for par in range (num1, num2 + 1):
    if par % 2 == 0:
        print(par)