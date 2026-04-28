preçototal = float(input("Digite o valor total da compra: "))
if preçototal <= 0:
    print("Valor inválido.")
else:
    print("""
Formas de pagamento
1. À vista (em espécie) - 15% de desconto
2. Débito - 10% de desconto
3. Crédito - 5% de desconto
""")

formapag = int(input("Digite a forma de pagamento (1-3): "))
if formapag <1 or formapag >3:
    print("Opção inválida")
else:
    if formapag == 1:
       desconto = preçototal*0.15
       valorfinal = preçototal - desconto
       print(f"O valor total da sua compra é: {valorfinal}")
    if formapag == 2:
       desconto = preçototal*0.10
       valorfinal = preçototal - desconto
       print(f"O valor total da sua compra é: {valorfinal}")
    if formapag == 3:
       desconto = preçototal*0.05
       valorfinal = preçototal - desconto
       print(f"O valor total da sua compra é: {valorfinal}")