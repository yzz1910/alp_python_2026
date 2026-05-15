cont = 0

while cont < 3:
    usuario = input("Digite seu nome de usuário: ")
    senha = input("Digite a senha: ")
    if usuario == "aluno" and senha == "12345":
        print("Acesso liberado.")
        break
    else:
        print("Tente novamente.")
        cont+=1
        if cont == 3:
            print("Você ultrapassou o limite de 3 tentativas, acesso bloqueado")