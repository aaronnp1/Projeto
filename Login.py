user = ''
pasw = ''
tip = ''
while True:
    cho = int(input('''
----- SEJA BEM-VINDO(A) -----
DIGITE 1 PARA FAZER SEU CADASTRO!
DIGITE 2 PARA FAZER SEU LOGIN!
'''))
    if (cho==1):
        print("Olá! Seja bem vindo(a) no programa! para se cadastrar, digite um nome, senha e dica da senha.")
        user = input("Qual será seu nome? Por favor escreva ele! ")
        pasw = input("Agora, qual sera sua senha? ")
        tip = input("Agora digite a dica! ")
        print("Cadastro realizado com sucesso!")
    elif (cho==2):
        print("Dica!",tip)
        print("Para fazer login, você tera que lembrar da sua senha e usuario! ")
        use2 = input("Digite o seu user ")
        if (use2==user):
            print("Agora, digite sua senha! ")
            pas2 = input("Digite sua senha! ")
            if (pas2==pasw):
                print("Login feito com sucesso! ")
                break
            else:
                print("Errado!")
                break
        
            
            
                         



