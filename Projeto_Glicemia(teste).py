emails = ['gabriel', 'joao', 'reinaldo']
senhas = ['123', 'gabriellopes', 'senhafraca']
glicemias = []


def inicio():
    pergunta = input('Olá bem vindo ao sistema de controle de glicemia!\n'
                     'Faça login => 1\n'
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
        print('Erro! Tente novamente!')
        inicio()




def fazerLogin():
    email = input('Coloque seu e-mail: ')
    senha = input('Agora sua senha: ')

    if email in emails and senha in senhas:
        print('Parabens! logado com sucesso!')
        glicemiaApp()
    else:
        print('Tente novamente!')
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
        print('Tente novamente!')
        fazerCadastro()


def glicemiaApp():
    print('Bem vindo ao App Controle de Glicemia!')
    pergunta = input('O que você quer fazer?\n'
                     'Adicionar um novo valor >>> 1\n'
                     'Ver suas medidas >>> 2\n'
                     'Ver um gráfico com as medidas >> 3\n'
                     'Sair do aplicativo >>> 4\n')

    if pergunta == '1':
        adicionar_glicemia = input('Adicione a sua glicemia (Ex: 124): ')
        if adicionar_glicemia.isnumeric():
            glicemias.append(adicionar_glicemia)
            print('Glicemia adicionada com sucesso!')
            dnv = input('Você quer adicionar mais?\n'
                        'Sim >>> 1'
                        'Não >>> 2'
                        'Sair do aplicativo totalmente >>> 3')
    elif pergunta == '4':
        print('Tudo bem! Muito obrigado!')
        exit()




inicio()
