print("Calculadora Simples")
print("1. Soma")
print("2. Subtração")
print("3. Multiplicação")
print("4. Divisão")

opcao = int(input("Escolha a operação (1/2/3/4): "))
num1 = float(input("digite o primeiro número: "))
num2 = float(input("digite o segundo número: "))

if opcao == 1:
    resultado = num1 + num2
    print (f"o resultado é {resultado}")
elif opcao == 2:
    resultado = num1 - num2
    print(f"o resultado é {resultado}")
elif opcao == 3:
    resultado = num1 * num2
    print(f"o resultado é {resultado}")
elif opcao == 4:
    resultado = num1/num2
    print(f"o resultado é {resultado}")