from time import sleep

# db
email_db = 'gab'
senha_db = '123'
# db

# inicio programa
def pergunta():
    pergunta = input('Você já tem cadastro?\nSim - 1\nNão - 2\n>>> ')  # pergunta se tem cadastro
    return pergunta

while True:
    if pergunta != '1' and pergunta != '2':
        while pergunta != '1' or pergunta != '2':
            print('Algo deu errado, tente novamente!\n')
            pergunta = input('Você já tem cadastro?\nSim - 1\nNão - 2\n>>> ')  # pergunta se tem cadastro
            if pergunta == '1' or pergunta == '2':
                break
    if pergunta == '1':
        email = input('Digite seu e-mail: ')
        senha = input('Digite sua senha: ')
        if email == email_db and senha == senha_db:
            print('Parabéns foi logado com sucesso!')
            break
        else:
            while senha != senha_db or email != email_db:
                print('Ops! Senha ou E-mail inválido, tente novamente...')
                email = input('Digite seu e-mail: ')
                senha = input('Digite sua senha: ')
            else:
                print('Logado com sucesso!')
                break
    elif pergunta == '2':
        ...  # Posteriormente com um db, fazer função de cadastro
