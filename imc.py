#calculadora imc
print("""
----------- Tabela de IMC -----------

menor que 18.5       | magreza
entre 18.5 e 24.9    | peso normal
entre 25.0 e 29.9    | sobrepeso
entre 30.0 e 39.9    | obesidade
acima de 40          | obesidade grave
------------------------------------
""")

peso = float(input("digite o seu peso: "))
altura = float(input("digite a sua altura: "))
imc = peso/(altura**2)

if imc < 18.5:
    print("Magreza")
elif imc < 25:
    print(f"peso normal, seu imc é: {imc :.2f}")
elif imc < 30:
    print(f"sobrepeso, seu imc é: {imc :.2f}")
elif imc < 40:
    print(f"obesidade, seu imc é: {imc :.2f}")
else:
    print(f"obesidade grave, seu imc é: {imc :.2f}")