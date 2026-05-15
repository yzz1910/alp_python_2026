par = 0
impar = 0

for cont in range(10):
    numero = int(input("Digite um número positivo: "))
    if numero %2 == 0:
        par += 1
    else:
        impar += 1
    
print(f"você digitou {par} números pares e {impar} números ímpares")