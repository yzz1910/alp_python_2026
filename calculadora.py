print("Calculadora Simples")
print("1. Soma")
print("2. Subtração")
print("3. Multiplicação")
print("4. Divisão")

opcao = float(input("Escolha a operação (1/2/3/4): "))
if opcao <1 or opcao >4:
    print("Operação inválida.")
else:
    print("Ok, agora digite os números.")
    num1 = float(input("Digite o primeiro número: "))
    num2 = float(input("Digite o segundo número: "))

    if opcao == 1:
        print(f"O resultado da sua operação é: {num1+num2}")
    elif opcao == 2:
        print(f"O resultado da sua operação é: {num1-num2}")
    elif opcao == 3:
        print(f"O resultado da sua operação é: {num1*num2}")
    elif opcao == 4:
        print(f"O resultado da sua operação é: {num1/num2}")