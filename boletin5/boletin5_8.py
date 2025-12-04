num1 = 0
num2 = 0
num_max = int(input("Dime un numero:"))
for num1 in range (0, num_max + 1):
    for num2 in range (num1, num_max + 1):
        print(num1, num2)
