num1 = int(input("digite o número 1: "))
num2 = int(input("digite o número 2: "))
num3 = int(input("digite o número 3: "))

if num1 == num2 or num2 == num3 or num1 == num3:
    exit()
if num1 > num2 and num1 > num3:
    print("o primeiro número é o maior")
if num2 > num1 and num2 > num3:
    print("o segundo número é o maior")
if num3 > num2 and num3 > num1:
    print("o terceiro número é o maior")