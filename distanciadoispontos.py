from math import sqrt

x1 = float(input("digite o valor de x1: "))
y1 = float(input("digite o valor de y1: "))

x2 = float(input("digite o valor de x2: "))
y2 = float(input("digite o valor de y2: "))

distancia = sqrt((x2-x1)**2 + (y2-y1)**2)

print(f"a distância entre os dois pontos é: {distancia:.2f}")