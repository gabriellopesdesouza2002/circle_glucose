from time import sleep
from matplotlib import pyplot

emails = ['gabriel', 'joao', 'reinaldo', 'gab']
senhas = ['123', 'gabriellopes', 'senhafraca']
glicemias_01 = []
glicemias_02 = []
glicemias_03 = []
glicemias_04 = []
glicemias_05 = []
glicemias_06 = []
glicemias_07 = []
glicemias_08 = []
glicemias_09 = []


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
    print('Para sair, digite "q" a qualquer momento ou "r" para recomeçar')
    email = input('Coloque seu e-mail: ')
    if email == 'q' or email == 'Q':
        print('Tudo bem! Muito obrigado!')
        exit()
    elif email == 'r' or email == 'R':
        fazerLogin()
    senha = input('Agora sua senha: ')
    if senha == 'q' and senha == 'Q':
        print('Tudo bem! Muito obrigado!')
        exit()
    elif senha == 'r' or senha == 'R':
        fazerLogin()
    elif email in emails and senha in senhas:
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
                print('Cadastro realizado com sucesso!\n')
                print('\033[1;32mFaça Login agora!\033[m')
                fazerLogin()
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
        addGlicemia()
    elif pergunta == '2':
        verMedidas()
    elif pergunta == '3':
        verGrafico()
    elif pergunta == '4':
        print('Tudo bem! Muito obrigado!')
        sleep(1)
        exit()
    else:
        print('\033[1;31mTente novamente!\033[m')
        glicemiaApp()


def addGlicemia():
    adicionar_glicemia = input('Adicione a sua glicemia (Ex: 124): ')
    periodo = input('Qual periodo foi feito a medição?\n'
                    'Ao levantar ➜ 1\n'
                    'Antes do almoço ➜ 2\n'
                    'Depois do almoço ➜ 3\n'
                    'Antes do lanche ➜ 4\n'
                    'Depois do lanche ➜ 5\n'
                    'Antes do jantar ➜ 6\n'
                    'Depois do jantar ➜ 7\n'
                    'Ao dormir ➜ 8\n'
                    'Sem Período Especificado ➜ 9\n'
                    '>>> ')

    if adicionar_glicemia.isnumeric():
        adicionar_glicemia = int(adicionar_glicemia)
        if adicionar_glicemia >= 40 and adicionar_glicemia <= 600:
            if periodo == '1':
                print('Você escolheu "Ao levantar"')
                sleep(1)
                glicemias_01.append(adicionar_glicemia)
                glicemiaApp()
            elif periodo == '2':
                print('Você escolheu "Antes do almoço"')
                sleep(1)
                glicemias_02.append(adicionar_glicemia)
                glicemiaApp()
            elif periodo == '3':
                print('Você escolheu "Depois do almoço"')
                sleep(1)
                glicemias_03.append(adicionar_glicemia)
                glicemiaApp()
            elif periodo == '4':
                print('Você escolheu "Antes do lanche"')
                sleep(1)
                glicemias_04.append(adicionar_glicemia)
                glicemiaApp()
            elif periodo == '5':
                print('Você escolheu "Depois do lanche"')
                sleep(1)
                glicemias_05.append(adicionar_glicemia)
                glicemiaApp()
            elif periodo == '6':
                print('Você escolheu "Antes do jantar"')
                sleep(1)
                glicemias_06.append(adicionar_glicemia)
                glicemiaApp()
            elif periodo == '7':
                print('Você escolheu "Depois do jantar"')
                sleep(1)
                glicemias_07.append(adicionar_glicemia)
                glicemiaApp()
            elif periodo == '8':
                print('Você escolheu "Ao dormir"')
                sleep(1)
                glicemias_08.append(adicionar_glicemia)
                glicemiaApp()
            elif periodo == '9':
                print('Você escolheu "Sem Período Especificado"')
                sleep(1)
                glicemias_09.append(adicionar_glicemia)
                glicemiaApp()
        else:
            print(f'\033[1;31mO valor: {adicionar_glicemia} é inválido. Tente novamente!\033[m')
            addGlicemia()
    else:
        print(f'\033[1;31mO valor: {adicionar_glicemia} é inválido. Tente novamente!\033[m')
        addGlicemia()


def verMedidas():
    escolha = input('Você quer ver os resultados de qual período?\n'
                    'Ao levantar ➜ 1\n'
                    'Antes do almoço ➜ 2\n'
                    'Depois do almoço ➜ 3\n'
                    'Antes do lanche ➜ 4\n'
                    'Depois do lanche ➜ 5\n'
                    'Antes do jantar ➜ 6\n'
                    'Depois do jantar ➜ 7\n'
                    'Ao dormir ➜ 8\n'
                    'Sem Período Especificado ➜ 9\n'
                    '>>> ')
    if escolha == '1':
        print(f'Mostrando glicemias do período: "Ao levantar"')
        sleep(1)
        if not glicemias_01:
            print('\033[1;31mNão há valores ainda aqui!\033[m')
            glicemiaApp()
        else:
            for glicemia in glicemias_01:
                print(glicemia, '\n')
            else:
                glicemiaApp()
    elif escolha == '2':
        print(f'Mostrando glicemias do período: "Antes do almoço"')
        sleep(1)
        if not glicemias_02:
            print('\033[1;31mNão há valores ainda aqui!\033[m')
            glicemiaApp()
        else:
            for glicemia in glicemias_02:
                print(glicemia, '\n')
            else:
                glicemiaApp()
    elif escolha == '3':
        print(f'Mostrando glicemias do período: "Depois do almoço"')
        sleep(1)
        if not glicemias_03:
            print('\033[1;31mNão há valores ainda aqui!\033[m')
            glicemiaApp()
        else:
            for glicemia in glicemias_03:
                print(glicemia, '\n')
            else:
                glicemiaApp()
    elif escolha == '4':
        print(f'Mostrando glicemias do período: "Antes do lanche"')
        sleep(1)
        if not glicemias_04:
            print('\033[1;31mNão há valores ainda aqui!\033[m')
            glicemiaApp()
        else:
            for glicemia in glicemias_04:
                print(glicemia, '\n')
            else:
                glicemiaApp()
    elif escolha == '5':
        print(f'Mostrando glicemias do período: "Depois do lanche"')
        sleep(1)
        if not glicemias_05:
            print('\033[1;31mNão há valores ainda aqui!\033[m')
            glicemiaApp()
        else:
            for glicemia in glicemias_05:
                print(glicemia, '\n')
            else:
                glicemiaApp()
    elif escolha == '6':
        print(f'Mostrando glicemias do período: "Antes do jantar"')
        sleep(1)
        if not glicemias_06:
            print('\033[1;31mNão há valores ainda aqui!\033[m')
            glicemiaApp()
        else:
            for glicemia in glicemias_06:
                print(glicemia, '\n')
            else:
                glicemiaApp()
    elif escolha == '7':
        print(f'Mostrando glicemias do período: "Depois do jantar"')
        sleep(1)
        if not glicemias_07:
            print('\033[1;31mNão há valores ainda aqui!\033[m')
            glicemiaApp()
        else:
            for glicemia in glicemias_07:
                print(glicemia, '\n')
            else:
                glicemiaApp()
    elif escolha == '8':
        print(f'Mostrando glicemias do período: "Ao dormir"')
        sleep(1)
        if not glicemias_08:
            print('\033[1;31mNão há valores ainda aqui!\033[m')
            glicemiaApp()
        else:
            for glicemia in glicemias_08:
                print(glicemia, '\n')
            else:
                glicemiaApp()
    elif escolha == '9':
        print(f'Mostrando glicemias do período: "Sem período especificado"')
        sleep(1)
        if not glicemias_09:
            print('\033[1;31mNão há valores ainda aqui!\033[m')
            glicemiaApp()
        else:
            for glicemia in glicemias_09:
                print(glicemia, '\n')
            else:
                glicemiaApp()
    else:
        print('\033[1;31mTente novamente!\033[m')
        verMedidas()


def verGrafico():
    escolha = input('De qual período quer ver o gráfico?\n'
                    'Ao levantar ➜ 1\n'
                    'Antes do almoço ➜ 2\n'
                    'Depois do almoço ➜ 3\n'
                    'Antes do lanche ➜ 4\n'
                    'Depois do lanche ➜ 5\n'
                    'Antes do jantar ➜ 6\n'
                    'Depois do jantar ➜ 7\n'
                    'Ao dormir ➜ 8\n'
                    'Sem Período Especificado ➜ 9\n'
                    'Todos os períodos'
                    '>>> ')

    if escolha == '1':
        print('Mostrando Gráfico de: Ao levantar.')
        if not glicemias_01:  # Aqui vê se a lista está vazia
            print('\033[1;31mNão há valores ainda aqui!\033[m')
            sleep(2)
            verGrafico()  # Volta para a função verGrafico()
        else:
            pyplot.plot(glicemias_01)  # Seleciona a lista com os dados
            pyplot.show()  # Mostra o gráfico.
            glicemiaApp()  # Quando acabar de mostrar o gráfico, volta ao menu inicial
    elif escolha == '2':
        print('Mostrando Gráfico de: Antes do almoço.')
        if not glicemias_02:
            print('\033[1;31mNão há valores ainda aqui!\033[m')
            sleep(2)
            verGrafico()
        else:
            pyplot.plot(glicemias_02)
            pyplot.show()
            glicemiaApp()
    elif escolha == '3':
        print('Mostrando Gráfico de: Depois do almoço.')
        if not glicemias_03:
            print('\033[1;31mNão há valores ainda aqui!\033[m')
            sleep(2)
            verGrafico()
        else:
            pyplot.plot(glicemias_03)
            pyplot.show()
            glicemiaApp()
    elif escolha == '4':
        print('Mostrando Gráfico de: Antes do lanche.')
        if not glicemias_04:
            print('\033[1;31mNão há valores ainda aqui!\033[m')
            sleep(2)
            verGrafico()
        else:
            pyplot.plot(glicemias_04)
            pyplot.show()
            glicemiaApp()
    elif escolha == '5':
        print('Mostrando Gráfico de: Depois do lanche.')
        if not glicemias_05:
            print('\033[1;31mNão há valores ainda aqui!\033[m')
            sleep(2)
            verGrafico()
        else:
            pyplot.plot(glicemias_05)
            pyplot.show()
            glicemiaApp()
    elif escolha == '6':
        print('Mostrando Gráfico de: Antes do jantar.')
        if not glicemias_06:
            print('\033[1;31mNão há valores ainda aqui!\033[m')
            sleep(2)
            verGrafico()
        else:
            pyplot.plot(glicemias_06)
            pyplot.show()
            glicemiaApp()
    elif escolha == '7':
        print('Mostrando Gráfico de: Depois do jantar.')
        if not glicemias_07:
            print('\033[1;31mNão há valores ainda aqui!\033[m')
            sleep(2)
            verGrafico()
        else:
            pyplot.plot(glicemias_07)
            pyplot.show()
            glicemiaApp()
    elif escolha == '8':
        print('Mostrando Gráfico de: Ao dormir.')
        if not glicemias_08:
            print('\033[1;31mNão há valores ainda aqui!\033[m')
            sleep(2)
            verGrafico()
        else:
            pyplot.plot(glicemias_08)
            pyplot.show()
            glicemiaApp()
    elif escolha == '9':
        print('Mostrando Gráfico de: Sem período especificado.')
        if not glicemias_09:
            print('\033[1;31mNão há valores ainda aqui!\033[m')
            sleep(2)
            verGrafico()
        else:
            pyplot.plot(glicemias_09)
            pyplot.show()
            glicemiaApp()
    else:
        print('\033[1;31mTente novamente!\033[m')
        verGrafico()


inicio()
