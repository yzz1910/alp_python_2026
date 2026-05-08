precoproduto = float(input("Digite o valor do produto: "))
if precoproduto <= 0:
    print("Digite um valor válido.")
    exit()
else:
    print("Agora digite a quantidade de produtos.")

quantidade = int(input("Digite quantos produtos você comprou: "))

if quantidade <= 0:
    print("Digite um valor válido.")
    exit()
else:
    print(f"O valor total da suas compras é: {precoproduto*quantidade}")