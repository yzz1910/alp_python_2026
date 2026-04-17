nota1 = float(input("digite o valor da sua primeira nota: "))
nota2 = float(input("digite o valor da sua segunda nota: "))
nota3 = float(input("digite o valor da sua terceira nota: "))

media = (nota1+nota2+nota3)/3

if media >= 7:
    print(f"Você está aprovado! Sua média é: {media :.1f}")
else:
    print(f"Você está reprovado! Sua média é: {media:.1f}")