print("""
Opções
1. Média ponderada
2. Quadrado da soma
3. Cubo do menor número
""")

opcao = float(input("Selecione uma opção de 1 a 3: "))
if opcao <1 or opcao >3:
    print("Opção inválida")
else:
    print("Agora digite os dois números positivos")
    num1 = float(input("Digite o primeiro número: "))
    if num1 <= 0:
        print("Número inválido!")
    num2 = float(input("Digite o segundo número: "))
    if num2 <= 0:
        print("Número inválido!")
    if opcao == 1:
        print(f"A média ponderada dos seus números é: {(num1*2 + num2*3)/(2+3)}")
    elif opcao == 2:
        print(f"A soma do quadrado dos seus números é: {(num1+num2)**2}")
    elif opcao == 3:
        if num1 > num2:
            print(f"O cubo do menor número é: {(num2)**3}")
        if num2 > num1:
            print(f"O cubo do menor número é: {(num1)**3}")
        if num1 == num2:
            print("Os dois números são iguais!")
