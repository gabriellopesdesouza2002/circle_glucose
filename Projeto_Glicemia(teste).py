from time import sleep

emails = ['gabriel', 'joao', 'reinaldo', 'gab']
senhas = ['123', 'gabriellopes', 'senhafraca']
glicemias = []

def inicio():
    pergunta = input('\n\033[1;92mOlá bem vindo ao sistema de controle de glicemia!\033[m\n\n'
                     'Faça login >>> 1\n'
                     'Faça um cadastro >>> 2\n'
                     'Sair do aplicativo >>> 3\n'
                     '>>> ')
    if pergunta == '1':
        fazerLogin()
    elif pergunta == '2':
        fazerCadastro()
    elif pergunta == '3':
        print('Tudo bem! Muito obrigado!')
        exit()
    else:
        print('\033[1;31mTente novamente!\033[m')
        inicio()




def fazerLogin():
    email = input('Coloque seu e-mail: ')
    senha = input('Agora sua senha: ')

    if email in emails and senha in senhas:
        print('\n\033[1;92mParabéns! logado com sucesso!\033[m\n')
        glicemiaApp()
    else:
        print('\033[1;31mTente novamente!\033[m')
        fazerLogin()


def fazerCadastro():
    print('Bem vindo a área de cadastro!')
    sair = input('Você deseja mesmo fazer um cadastro?\n'
                 'Sim >>> 1\n'
                 'Não, voltar ao Login >>> 2\n'
                 'Sair do aplicativo >>> 3\n'
                 '>>> ')
    if sair == '1':
        email_novo = input('Digite o novo e-mail: ')
        senha_novo = input('Digite a sua senha: ')
        senha_novo_verificada = input('Digite a mesma senha: ')

        if senha_novo == senha_novo_verificada:
            if email_novo in emails:
                print('O email já existe no nosso banco de dados! Tente novamente.')
                fazerCadastro()
            else:
                emails.append(email_novo)
                senhas.append(senha_novo_verificada)
                print('Cadastro realizado com sucesso!')
                glicemiaApp()
    elif sair == '2':
        inicio()
    elif sair == '3':
        print('Tudo bem! Muito obrigado!')
        exit()
    else:
        print('\033[1;31mTente novamente!\033[m')
        fazerCadastro()


def glicemiaApp():
    pergunta = input('O que você quer fazer?\n'
                     'Adicionar um novo valor >>> 1\n'
                     'Ver suas medidas >>> 2\n'
                     'Ver um gráfico com as medidas >> 3\n'
                     'Sair do aplicativo >>> 4\n'
                     '>>> ')

    if pergunta == '1':
        adicionar_glicemia = input('Adicione a sua glicemia (Ex: 124): ')
        periodo = input('Qual periodo foi feito a medição? '
                        '')
        if adicionar_glicemia.isnumeric():
            glicemias.append(adicionar_glicemia)
            print('\033[1;32mGlicemia adicionada com sucesso!\033[m\n')
            glicemiaApp()
        else:
            print(f'\033[1;31mO valor: {adicionar_glicemia} é inválido. Tente novamente!\033[m')
            glicemiaApp()
    elif pergunta == '2':
        for glicemia in glicemias:
            print(f'\033[1;32m{glicemia}\033[m\n')
        sleep(2)
        glicemiaApp()
    elif pergunta == '4':
        print('Tudo bem! Muito obrigado!')
        exit()




inicio()
