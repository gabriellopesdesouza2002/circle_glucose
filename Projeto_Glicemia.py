from time import sleep, gmtime, strftime
from matplotlib import pyplot
import getpass
emails = ['gab@.com', 'gab']
senhas = ['123']
glicemias_01 = []
glicemias_01_hora = []
glicemias_02 = []
glicemias_02_hora = []
glicemias_03 = []
glicemias_03_hora = []
glicemias_04 = []
glicemias_04_hora = []
glicemias_05 = []
glicemias_05_hora = []
glicemias_06 = []
glicemias_06_hora = []
glicemias_07 = []
glicemias_07_hora = []
glicemias_08 = []
glicemias_08_hora = []
glicemias_09 = []
glicemias_09_hora = []


def fechaApp():
    print('Tudo bem! Muito obrigado!')
    exit()


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
        fechaApp()
    else:
        print('\033[1;31mTente novamente!\033[m')
        inicio()


def fazerLogin():
    print('\033[1;32mBem vindo a área de Login!\033[m')
    print('Para sair, digite "q" a qualquer momento ou "r" para recomeçar ou "v" para voltar ao menu anterior')
    email = input('Coloque seu e-mail: ')
    if email == 'q' or email == 'Q':
        fechaApp()
    elif email == 'r' or email == 'R':
        fazerLogin()
    elif email == 'v' or email == 'V':
        inicio()
    senha = getpass.getpass('Digite sua senha (Não será mostrada!): ')
    if senha == 'q' and senha == 'Q':
        fechaApp()
    elif senha == 'r' or senha == 'R':
        fazerLogin()
    elif senha == 'v' or senha == 'V':
        inicio()
    elif email in emails and senha in senhas:
        print('\n\033[1;92mParabéns! logado com sucesso!\033[m\n')
        glicemiaApp()
    else:
        print('\033[1;31mTente novamente!\033[m')
        fazerLogin()


def fazerCadastro():
    print('\033[1;32mBem vindo a área de cadastro!\033[m\n')
    print('Caso queira sair digite "q", "r" para reiniciar ou "l" para ir ao login')
    email_novo = input('Digite o novo e-mail: ')
    if email_novo == 'q' or email_novo == 'Q':
        fechaApp()
    elif email_novo == 'r' or email_novo == 'R':
        fazerCadastro()
    elif email_novo == 'l' or email_novo == 'L':
        fazerLogin()
    elif not email_novo in '@' and '.com':
        print('\033[1;31mSeu E-mail não está correto!\033[m')
        fazerCadastro()
    senha_novo = input('Digite a sua senha: ')
    if senha_novo == 'q' or senha_novo == 'Q':
        fechaApp()
    elif senha_novo == 'r' or senha_novo == 'R':
        fazerCadastro()
    elif senha_novo == 'l' or senha_novo == 'L':
        fazerLogin()
    senha_novo_verificada = input('Digite a mesma senha: ')
    if senha_novo_verificada == 'q' or senha_novo_verificada == 'Q':
        fechaApp()
    elif senha_novo_verificada == 'r' or senha_novo_verificada == 'R':
        fazerCadastro()
    elif senha_novo_verificada == 'l' or senha_novo_verificada == 'L':
        fazerLogin()

    if senha_novo == senha_novo_verificada and len(senha_novo_verificada) >= 3:
        if email_novo in emails:
            print('O email já existe no nosso banco de dados! Tente novamente.')
            fazerCadastro()
        else:
            emails.append(email_novo)
            senhas.append(senha_novo_verificada)
            print('\033[1;32mCadastro realizado com sucesso!\033[m\n')
            print('\033[1;32mFaça Login agora!\033[m')
            fazerLogin()
    else:
        print('\033[1;31mTente novamente!\033[m\n')
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
        fechaApp()
    else:
        print('\033[1;31mTente novamente!\033[m')
        glicemiaApp()


def addGlicemia():
    print('Caso queira sair digite "q", "r" para reiniciar ou "v" para voltar ao menu anterior\n')
    adicionar_glicemia = input('Adicione a sua glicemia (Ex: 124): ')
    if adicionar_glicemia == 'q' or adicionar_glicemia == 'Q':
        fechaApp()
    elif adicionar_glicemia == 'r' or adicionar_glicemia == 'R':
        fazerCadastro()
    elif adicionar_glicemia == 'l' or adicionar_glicemia == 'L':
        fazerLogin()
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
    if periodo == 'q' or periodo == 'Q':
        fechaApp()
    elif periodo == 'r' or periodo == 'R':
        fazerCadastro()
    elif periodo == 'l' or periodo == 'L':
        fazerLogin()

    if adicionar_glicemia.isnumeric():
        adicionar_glicemia = int(adicionar_glicemia)
        if adicionar_glicemia >= 40 and adicionar_glicemia <= 600:
            if periodo == '1':
                print('Você escolheu "Ao levantar"')
                sleep(1)
                glicemias_01.append(adicionar_glicemia)
                glicemias_01_hora.append(strftime("%d | %H:%M:%S", gmtime()))
                glicemiaApp()
            elif periodo == '2':
                print('Você escolheu "Antes do almoço"')
                sleep(1)
                glicemias_02.append(adicionar_glicemia)
                glicemias_02_hora.append(strftime("%d | %H:%M:%S", gmtime()))
                glicemiaApp()
            elif periodo == '3':
                print('Você escolheu "Depois do almoço"')
                sleep(1)
                glicemias_03.append(adicionar_glicemia)
                glicemias_03_hora.append(strftime("%d | %H:%M:%S", gmtime()))
                glicemiaApp()
            elif periodo == '4':
                print('Você escolheu "Antes do lanche"')
                sleep(1)
                glicemias_04.append(adicionar_glicemia)
                glicemias_04_hora.append(strftime("%d | %H:%M:%S", gmtime()))
                glicemiaApp()
            elif periodo == '5':
                print('Você escolheu "Depois do lanche"')
                sleep(1)
                glicemias_05.append(adicionar_glicemia)
                glicemias_05_hora.append(strftime("%d | %H:%M:%S", gmtime()))
                glicemiaApp()
            elif periodo == '6':
                print('Você escolheu "Antes do jantar"')
                sleep(1)
                glicemias_06.append(adicionar_glicemia)
                glicemias_06_hora.append(strftime("%d | %H:%M:%S", gmtime()))
                glicemiaApp()
            elif periodo == '7':
                print('Você escolheu "Depois do jantar"')
                sleep(1)
                glicemias_07.append(adicionar_glicemia)
                glicemias_07_hora.append(strftime("%d | %H:%M:%S", gmtime()))
                glicemiaApp()
            elif periodo == '8':
                print('Você escolheu "Ao dormir"')
                sleep(1)
                glicemias_08.append(adicionar_glicemia)
                glicemias_08_hora.append(strftime("%d | %H:%M:%S", gmtime()))
                glicemiaApp()
            elif periodo == '9':
                print('Você escolheu "Sem Período Especificado"')
                sleep(1)
                glicemias_09.append(adicionar_glicemia)
                glicemias_09_hora.append(strftime("%d | %H:%M:%S", gmtime()))
                glicemiaApp()
        else:
            print(f'\033[1;31mO valor: {adicionar_glicemia} é inválido. Tente novamente!\033[m')
            addGlicemia()
    else:
        print(f'\033[1;31mO valor: {adicionar_glicemia} é inválido. Tente novamente!\033[m')
        addGlicemia()


def verMedidas():
    print('Caso queira sair digite "q", "r" para reiniciar ou "v" para voltar ao menu anterior\n')
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
                    'Sair totalmente do aplicativo ➜ "q"\n'
                    'Reiniciar esse menu ➜ "r"\n'
                    'Voltar ao menu anterior ➜ "v"\n'
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
    elif escolha == 'q':
        fechaApp()
    elif escolha == 'r':
        verMedidas()
    elif escolha == 'v':
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
            pyplot.plot(glicemias_01_hora, glicemias_01)  # Seleciona a lista com os dados
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
