usuario = input("digite seu nome de usuário: ")
senha = input("digite sua senha: ")

if usuario == "aluno" and senha == "aluno@ifpi":
    print(f"Seja bem vindo,{usuario}")
else:
    print("acesso negado")