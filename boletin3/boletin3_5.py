num1 = int(input("Dime un número:"))
num2 = int(input("Dime un número:"))
num3 = int(input("Dime un número:"))

if num1 > num2 and num1 > num3:
    print(f"{num1} es el mayor")

elif num2 > num1 and num2 > num3:
    print(f"{num2} es el mayor")

if num3 > num1 and num3 > num2:
    print(f"{num3} es el mayor")
