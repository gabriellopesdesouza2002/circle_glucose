from time import sleep, gmtime, strftime

from matplotlib import pyplot

import dados  # importa as listas simulando um db (Que limpa ao reiniciar o programa)


def inicio():  # Função que inicia o aplicativo
    pergunta = input('\n\033[1;92mOlá Bem Vindo ao Circle Glucose!\nSeu Assistente de Glicemia!\033[m\n\n'
                     'Faça Login >>> 1\n'
                     'Faça Seu Cadastro >>> 2\n'
                     'Sair >>> 3\n'
                     '>>> ')
    if pergunta == '1':  # Verifica se é login e vai pra função Login
        login()
    elif pergunta == '2':  # Verifica se é cadastro
        fazerCadastro()
    elif pergunta == '3':  # Verifica se usuário quer fechar software
        fechaApp()
    else:  # Se tudo falso, tenta novamente
        print('\033[1;31mTente novamente!\033[m')
        sleep(1)
        inicio()


def login():  # Função para fazer login
    print("\033[1;32m=\033[m" * 30)
    print('\033[1;32mBem vindo a área de Login!\033[m')
    print("\033[1;32m=\033[m" * 30, '\n')

    print('Digite "q" para sair, "r" para reiniciar ou "v" para voltar ao menu anterior')
    email = input('Coloque seu e-mail: ')
    if email == 'q' or email == 'Q':  # se email for q, significa que o usuário que sair do software
        fechaApp()
    elif email == 'r' or email == 'R':  # se for r, significa que a função será executada do 0
        login()
    elif email == 'v' or email == 'V':  # se v, volta ao menu anterior
        inicio()
    senha = input('Digite sua senha: ')
    if senha == 'q' and senha == 'Q':  # se senha for q, significa que o usuário que sair do software
        fechaApp()
    elif senha == 'r' or senha == 'R':  # se for r, significa que a função será executada do 0
        login()
    elif senha == 'v' or senha == 'V':  # se v, volta ao menu anterior
        inicio()
    elif email in dados.emails and senha in dados.senhas:  # se o email e a senha existir na base de dados, entra
        print('\n\033[1;92mParabéns! conectado com sucesso!\033[m\n')
        glicemiaApp()
    else:  # senão, volta ao menu anterior
        print('\033[1;31mTente novamente!\033[m')
        sleep(1)
        login()


def fazerCadastro():
    print('\033[1;32mBem vindo a área de cadastro!\033[m\n')
    print('Digite "q" para sair, "r" para reiniciar ou "v" para voltar ao menu anterior')

    email_novo = input('Digite o novo e-mail: ')

    if email_novo == 'q' or email_novo == 'Q':
        fechaApp()
    elif email_novo == 'r' or email_novo == 'R':
        fazerCadastro()
    elif email_novo == 'v' or email_novo == 'V':
        inicio()
    elif email_novo and '@' and '.com' in email_novo:
        senha_novo = input('Digite a sua senha: ')
        if senha_novo == 'q' or senha_novo == 'Q':
            fechaApp()
        elif senha_novo == 'r' or senha_novo == 'R':
            fazerCadastro()
        elif senha_novo == 'v' or senha_novo == 'V':
            inicio()
        else:
            senha_novo_verificada = input('Digite a mesma senha: ')
            if senha_novo_verificada == 'q' or senha_novo_verificada == 'Q':
                fechaApp()
            elif senha_novo_verificada == 'r' or senha_novo_verificada == 'R':
                fazerCadastro()
            elif senha_novo_verificada == 'v' or senha_novo_verificada == 'V':
                inicio()
            else:
                if senha_novo == senha_novo_verificada and len(senha_novo_verificada) >= 3:
                    if email_novo in dados.emails:
                        print('\n\033[1;31mO email já existe no nosso banco de dados! Tente novamente.\033[m\n')
                        sleep(1)
                        fazerCadastro()
                    else:
                        dados.emails.append(email_novo)
                        dados.senhas.append(senha_novo_verificada)
                        print('\033[1;32mCadastro realizado com sucesso!\033[m\n')
                        print('\033[1;32mFaça Login agora!\033[m')
                        login()
                else:
                    print('As senhas não combinam ou a senha é menor que 4 caracteres!')
                    fazerCadastro()

    else:
        print('\033[1;31mE-mail inválido, tente novamente!\033[m\n')
        sleep(1)
        fazerCadastro()


def glicemiaApp():
    pergunta = input('O que você quer fazer?\n\n'
                     'Adicionar um novo valor >>> 1\n'
                     'Ver suas medidas >>> 2\n'
                     'Ver um gráfico com as medidas >> 3\n'
                     'Ver a média de suas medidas >> 4\n'
                     'Fazer Logoff (Login / Cadastro) >>> 5\n'
                     'Configurações avançadas >>> 6\n'
                     'Sair >>> 7\n'
                     '>>> ')

    if pergunta == '1':
        addValor()
    elif pergunta == '2':
        verMedidas()
    elif pergunta == '3':
        verGrafico()
    elif pergunta == '4':
        verMedia()
    elif pergunta == '5':
        inicio()
    elif pergunta == '6':
        configs()
    elif pergunta == '7':
        fechaApp()
    else:
        print('\033[1;31mTente novamente!\033[m')
        sleep(1)
        glicemiaApp()


def addValor():
    print('Caso queira sair digite "q", "r" para reiniciar ou "v" para voltar ao menu anterior\n')
    adicionar_glicemia = input('Adicione a sua glicemia (Ex: 124): ')

    if adicionar_glicemia == 'q' or adicionar_glicemia == 'Q':
        fechaApp()
    elif adicionar_glicemia == 'r' or adicionar_glicemia == 'R':
        addValor()
    elif adicionar_glicemia == 'v' or adicionar_glicemia == 'V':
        glicemiaApp()
    elif adicionar_glicemia.isnumeric():
        adicionar_glicemia = int(adicionar_glicemia)  # transforma o valor de glicemia para número inteiro
        if 10 <= adicionar_glicemia <= 925:  # Verifica se a glicemia está entre 10 e 925
            def escolhe_periodo():  # função add para não fazer o usuário colocar novamente a glicemia em caso de erro
                periodo = input('Qual período foi feito a medição?\n'
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
                if periodo == '1':
                    print('Você escolheu "Ao levantar"\n')
                    sleep(1)
                    dados.glicemias_01.append(adicionar_glicemia)
                    dados.glicemias_01_hora.append(strftime("%d | %H:%M:%S", gmtime()))
                    glicemiaApp()
                elif periodo == '2':
                    print('Você escolheu "Antes do almoço"\n')
                    sleep(1)
                    dados.glicemias_02.append(adicionar_glicemia)
                    dados.glicemias_02_hora.append(strftime("%d | %H:%M:%S", gmtime()))
                    glicemiaApp()
                elif periodo == '3':
                    print('Você escolheu "Depois do almoço"\n')
                    sleep(1)
                    dados.glicemias_03.append(adicionar_glicemia)
                    dados.glicemias_03_hora.append(strftime("%d | %H:%M:%S", gmtime()))
                    glicemiaApp()
                elif periodo == '4':
                    print('Você escolheu "Antes do lanche"\n')
                    sleep(1)
                    dados.glicemias_04.append(adicionar_glicemia)
                    dados.glicemias_04_hora.append(strftime("%d | %H:%M:%S", gmtime()))
                    glicemiaApp()
                elif periodo == '5':
                    print('Você escolheu "Depois do lanche"\n')
                    sleep(1)
                    dados.glicemias_05.append(adicionar_glicemia)
                    dados.glicemias_05_hora.append(strftime("%d | %H:%M:%S", gmtime()))
                    glicemiaApp()
                elif periodo == '6':
                    print('Você escolheu "Antes do jantar"\n')
                    sleep(1)
                    dados.glicemias_06.append(adicionar_glicemia)
                    dados.glicemias_06_hora.append(strftime("%d | %H:%M:%S", gmtime()))
                    glicemiaApp()
                elif periodo == '7':
                    print('Você escolheu "Depois do jantar"\n')
                    sleep(1)
                    dados.glicemias_07.append(adicionar_glicemia)
                    dados.glicemias_07_hora.append(strftime("%d | %H:%M:%S", gmtime()))
                    glicemiaApp()
                elif periodo == '8':
                    print('Você escolheu "Ao dormir"\n')
                    sleep(1)
                    dados.glicemias_08.append(adicionar_glicemia)
                    dados.glicemias_08_hora.append(strftime("%d | %H:%M:%S", gmtime()))
                    glicemiaApp()
                elif periodo == '9':
                    print('Você escolheu "Sem Período Especificado"\n')
                    sleep(1)
                    dados.glicemias_09.append(adicionar_glicemia)
                    dados.glicemias_09_hora.append(strftime("%d | %H:%M:%S", gmtime()))
                    glicemiaApp()
                else:
                    print(f'\033[1;31mO periodo especificado, não é válido, tente novamente!\033[m')
                    sleep(1)
                    escolhe_periodo()
            escolhe_periodo()
        else:
            print(f'\033[1;31mO valor: ({adicionar_glicemia}) é inválido! Tente novamente!\033[m')
            sleep(1)
            addValor()
    else:
        print(f'\033[1;31mO valor: ({adicionar_glicemia}) é inválido. Tente novamente!\033[m')
        sleep(1)
        addValor()


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
                    'Ver todas as medidas ➜ "a"\n'
                    '>>> ')
    if escolha == 'q':
        fechaApp()
    elif escolha == 'r':
        verMedidas()
    elif escolha == 'v':
        glicemiaApp()
    elif escolha == '1':
        print(f'Mostrando glicemias do período: "Ao levantar"')
        sleep(1)
        if not dados.glicemias_01:
            print('\033[1;31mNão há valores ainda aqui!\033[m')
            glicemiaApp()
        else:
            for glicemia in dados.glicemias_01:
                print(glicemia, '\n')
            else:
                glicemiaApp()
    elif escolha == '2':
        print(f'Mostrando glicemias do período: "Antes do almoço"')
        sleep(1)
        if not dados.glicemias_02:
            print('\033[1;31mNão há valores ainda aqui!\033[m')
            glicemiaApp()
        else:
            for glicemia in dados.glicemias_02:
                print(glicemia, '\n')
            else:
                glicemiaApp()
    elif escolha == '3':
        print(f'Mostrando glicemias do período: "Depois do almoço"')
        sleep(1)
        if not dados.glicemias_03:
            print('\033[1;31mNão há valores ainda aqui!\033[m')
            glicemiaApp()
        else:
            for glicemia in dados.glicemias_03:
                print(glicemia, '\n')
            else:
                glicemiaApp()
    elif escolha == '4':
        print(f'Mostrando glicemias do período: "Antes do lanche"')
        sleep(1)
        if not dados.glicemias_04:
            print('\033[1;31mNão há valores ainda aqui!\033[m')
            glicemiaApp()
        else:
            for glicemia in dados.glicemias_04:
                print(glicemia, '\n')
            else:
                glicemiaApp()
    elif escolha == '5':
        print(f'Mostrando glicemias do período: "Depois do lanche"')
        sleep(1)
        if not dados.glicemias_05:
            print('\033[1;31mNão há valores ainda aqui!\033[m')
            glicemiaApp()
        else:
            for glicemia in dados.glicemias_05:
                print(glicemia, '\n')
            else:
                glicemiaApp()
    elif escolha == '6':
        print(f'Mostrando glicemias do período: "Antes do jantar"')
        sleep(1)
        if not dados.glicemias_06:
            print('\033[1;31mNão há valores ainda aqui!\033[m')
            glicemiaApp()
        else:
            for glicemia in dados.glicemias_06:
                print(glicemia, '\n')
            else:
                glicemiaApp()
    elif escolha == '7':
        print(f'Mostrando glicemias do período: "Depois do jantar"')
        sleep(1)
        if not dados.glicemias_07:
            print('\033[1;31mNão há valores ainda aqui!\033[m')
            glicemiaApp()
        else:
            for glicemia in dados.glicemias_07:
                print(glicemia, '\n')
            else:
                glicemiaApp()
    elif escolha == '8':
        print(f'Mostrando glicemias do período: "Ao dormir"')
        sleep(1)
        if not dados.glicemias_08:
            print('\033[1;31mNão há valores ainda aqui!\033[m')
            glicemiaApp()
        else:
            for glicemia in dados.glicemias_08:
                print(glicemia, '\n')
            else:
                glicemiaApp()
    elif escolha == '9':
        print(f'Mostrando glicemias do período: "Sem período especificado"')
        sleep(1)
        if not dados.glicemias_09:
            print('\033[1;31mNão há valores ainda aqui!\033[m')
            glicemiaApp()
        else:
            for glicemia in dados.glicemias_09:
                print(glicemia, '\n')
            else:
                glicemiaApp()
    elif escolha == 'a':
        print(f'Mostrando glicemias de: Todos os períodos.')
        sleep(1)
        for periodo, lista in dados.dicio_glicemia.items():
            print(periodo)
            if not lista:
                print('\tSem valores atualmente...\n')
            else:
                for glicemias in lista:
                    print(f'\t{glicemias}')
        else:
            print('Voltando para o menu inicial...\n')
            sleep(2)
            glicemiaApp()
    else:
        print('\033[1;31mTente novamente!\033[m')
        sleep(1)
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
                    'Sair ➜ "q"\n'
                    'Reiniciar esse menu ➜ "r"\n'
                    'Voltar ao menu anterior ➜ "v"\n'
                    '>>> ')

    if escolha == '1':
        print('Mostrando Gráfico de: Ao levantar.')
        if not dados.glicemias_01:  # Aqui vê se a lista está vazia
            print('\033[1;31mNão há valores ainda aqui!\033[m')
            sleep(2)
            verGrafico()  # Volta para a função verGrafico()
        else:
            pyplot.plot(dados.glicemias_01_hora, dados.glicemias_01)  # Seleciona a lista com os dados
            pyplot.show()  # Mostra o gráfico.
            glicemiaApp()  # Quando acabar de mostrar o gráfico, volta ao menu inicial
    elif escolha == '2':  # O mesmo processo até o if escolha == 'q' or escolha == 'Q'
        print('Mostrando Gráfico de: Antes do almoço.')
        if not dados.glicemias_02:
            print('\033[1;31mNão há valores ainda aqui!\033[m')
            sleep(2)
            verGrafico()
        else:
            pyplot.plot(dados.glicemias_02)
            pyplot.show()
            glicemiaApp()
    elif escolha == '3':
        print('Mostrando Gráfico de: Depois do almoço.')
        if not dados.glicemias_03:
            print('\033[1;31mNão há valores ainda aqui!\033[m')
            sleep(2)
            verGrafico()
        else:
            pyplot.plot(dados.glicemias_03)
            pyplot.show()
            glicemiaApp()
    elif escolha == '4':
        print('Mostrando Gráfico de: Antes do lanche.')
        if not dados.glicemias_04:
            print('\033[1;31mNão há valores ainda aqui!\033[m')
            sleep(2)
            verGrafico()
        else:
            pyplot.plot(dados.glicemias_04)
            pyplot.show()
            glicemiaApp()
    elif escolha == '5':
        print('Mostrando Gráfico de: Depois do lanche.')
        if not dados.glicemias_05:
            print('\033[1;31mNão há valores ainda aqui!\033[m')
            sleep(2)
            verGrafico()
        else:
            pyplot.plot(dados.glicemias_05)
            pyplot.show()
            glicemiaApp()
    elif escolha == '6':
        print('Mostrando Gráfico de: Antes do jantar.')
        if not dados.glicemias_06:
            print('\033[1;31mNão há valores ainda aqui!\033[m')
            sleep(2)
            verGrafico()
        else:
            pyplot.plot(dados.glicemias_06)
            pyplot.show()
            glicemiaApp()
    elif escolha == '7':
        print('Mostrando Gráfico de: Depois do jantar.')
        if not dados.glicemias_07:
            print('\033[1;31mNão há valores ainda aqui!\033[m')
            sleep(2)
            verGrafico()
        else:
            pyplot.plot(dados.glicemias_07)
            pyplot.show()
            glicemiaApp()
    elif escolha == '8':
        print('Mostrando Gráfico de: Ao dormir.')
        if not dados.glicemias_08:
            print('\033[1;31mNão há valores ainda aqui!\033[m')
            sleep(2)
            verGrafico()
        else:
            pyplot.plot(dados.glicemias_08)
            pyplot.show()
            glicemiaApp()
    elif escolha == '9':
        print('Mostrando Gráfico de: Sem período especificado.')
        if not dados.glicemias_09:
            print('\033[1;31mNão há valores ainda aqui!\033[m')
            sleep(2)
            verGrafico()
        else:
            pyplot.plot(dados.glicemias_09)
            pyplot.show()
            glicemiaApp()
    if escolha == 'q' or escolha == 'Q':
        fechaApp()  # Caso escolha seja "q" ou "Q" sairá do programa
    elif escolha == 'r' or escolha == 'R':
        verGrafico()  # Caso escolha seja "r" ou "R" reiniciará a função do zero
    elif escolha == 'v' or escolha == 'V':
        glicemiaApp()  # Caso escolha seja "v" ou "V" voltará um menu (função) anterior
    else:
        print('\033[1;31mTente novamente!\033[m')
        sleep(1)
        verGrafico()  # Caso todas as verificações sejam falsas, o usuário digitou algo que não é válido!


def verMedia():
    print('\033[1;32m=\033[m' * 30)
    print('\033[1;32mVer médias das suas medidas\033[m')
    print('\033[1;32m=\033[m' * 30, '\n')

    escolha = input('De qual periodo você quer ver a média?\n\n'
                    'Ao levantar ➜ 1\n'
                    'Antes do almoço ➜ 2\n'
                    'Depois do almoço ➜ 3\n'
                    'Antes do lanche ➜ 4\n'
                    'Depois do lanche ➜ 5\n'
                    'Antes do jantar ➜ 6\n'
                    'Depois do jantar ➜ 7\n'
                    'Ao dormir ➜ 8\n'
                    'Sem Período Especificado ➜ 9\n'
                    'Sair ➜ "q"\n'
                    'Reiniciar esse menu ➜ "r"\n'
                    'Voltar ao menu anterior ➜ "v"\n'
                    '>>> ')
    if escolha == '1':
        print('Você escolheu "Ao levantar".')
        if not dados.glicemias_01 or len(dados.glicemias_01) < 2:
            print(f'Ainda há {len(dados.glicemias_01)} glicemias atualmente...\n')
            sleep(1)
            print('Voltando...')
            sleep(1)
            verMedia()
        else:
            soma = 0
            for glicemia in dados.glicemias_01:
                soma += glicemia  # soma os valores das glicemias que estão na lista
            else:
                media = soma / len(dados.glicemias_01)  # faz a equação para fazer a média
                print(f'A sua média no periodo de "Ao levantar" é {media:.0f}')
                sleep(1)
                print(f'Voltando para o menu principal...')
                sleep(1)
                glicemiaApp()
    elif escolha == '2':
        print('Você escolheu "Antes do almoço".')
        if not dados.glicemias_02 or len(dados.glicemias_02) < 2:
            print(f'Ainda há {len(dados.glicemias_02)} glicemias atualmente...\n')
            sleep(1)
            print('Voltando...')
            sleep(1)
            verMedia()
        else:
            soma = 0
            for glicemia in dados.glicemias_02:
                soma += glicemia  # soma os valores das glicemias que estão na lista
            else:
                media = soma / len(dados.glicemias_02)  # faz a equação para fazer a média
                print(f'A sua média no periodo de "Antes do almoço" é {media:.0f}')
                sleep(1)
                print(f'Voltando para o menu principal...')
                sleep(1)
                glicemiaApp()
    elif escolha == '3':
        print('Você escolheu "Depois do almoço".')
        if not dados.glicemias_03 or len(dados.glicemias_03) < 2:
            print(f'Ainda há {len(dados.glicemias_03)} glicemias atualmente...\n')
            sleep(1)
            print('Voltando...')
            sleep(1)
            verMedia()
        else:
            soma = 0
            for glicemia in dados.glicemias_03:
                soma += glicemia  # soma os valores das glicemias que estão na lista
            else:
                media = soma / len(dados.glicemias_03)  # faz a equação para fazer a média
                print(f'A sua média no periodo de "Depois do almoço" é {media:.0f}')
                sleep(1)
                print(f'Voltando para o menu principal...')
                sleep(1)
                glicemiaApp()
    elif escolha == '4':
        print('Você escolheu "Antes do lanche".')
        if not dados.glicemias_04 or len(dados.glicemias_04) < 2:
            print(f'Ainda há {len(dados.glicemias_04)} glicemias atualmente...\n')
            sleep(1)
            print('Voltando...')
            sleep(1)
            verMedia()
        else:
            soma = 0
            for glicemia in dados.glicemias_04:
                soma += glicemia  # soma os valores das glicemias que estão na lista
            else:
                media = soma / len(dados.glicemias_04)  # faz a equação para fazer a média
                print(f'A sua média no periodo de "Antes do lanche" é {media:.0f}')
                sleep(1)
                print(f'Voltando para o menu principal...')
                sleep(1)
                glicemiaApp()
    elif escolha == '5':
        print('Você escolheu "Depois do lanche".')
        if not dados.glicemias_05 or len(dados.glicemias_05) < 2:
            print(f'Ainda há {len(dados.glicemias_05)} glicemias atualmente...\n')
            sleep(1)
            print('Voltando...')
            sleep(1)
            verMedia()
        else:
            soma = 0
            for glicemia in dados.glicemias_05:
                soma += glicemia  # soma os valores das glicemias que estão na lista
            else:
                media = soma / len(dados.glicemias_05)  # faz a equação para fazer a média
                print(f'A sua média no periodo de "Depois do lanche" é {media:.0f}')
                sleep(1)
                print(f'Voltando para o menu principal...')
                sleep(1)
                glicemiaApp()
    elif escolha == '5':
        print('Você escolheu "Depois do lanche".')
        if not dados.glicemias_05 or len(dados.glicemias_05) < 2:
            print(f'Ainda há {len(dados.glicemias_05)} glicemias atualmente...\n')
            sleep(1)
            print('Voltando...')
            sleep(1)
            verMedia()
        else:
            soma = 0
            for glicemia in dados.glicemias_05:
                soma += glicemia  # soma os valores das glicemias que estão na lista
            else:
                media = soma / len(dados.glicemias_05)  # faz a equação para fazer a média
                print(f'A sua média no periodo de "Depois do lanche" é {media:.0f}')
                sleep(1)
                print(f'Voltando para o menu principal...')
                sleep(1)
                glicemiaApp()
    elif escolha == '6':
        print('Você escolheu "Antes do jantar".')
        if not dados.glicemias_06 or len(dados.glicemias_06) < 2:
            print(f'Ainda há {len(dados.glicemias_06)} glicemias atualmente...\n')
            sleep(1)
            print('Voltando...')
            sleep(1)
            verMedia()
        else:
            soma = 0
            for glicemia in dados.glicemias_06:
                soma += glicemia  # soma os valores das glicemias que estão na lista
            else:
                media = soma / len(dados.glicemias_06)  # faz a equação para fazer a média
                print(f'A sua média no periodo de "Antes do jantar" é {media:.0f}')
                sleep(1)
                print(f'Voltando para o menu principal...')
                sleep(1)
                glicemiaApp()
    elif escolha == '7':
        print('Você escolheu "Depois do jantar".')
        if not dados.glicemias_07 or len(dados.glicemias_07) < 2:
            print(f'Ainda há {len(dados.glicemias_07)} glicemias atualmente...\n')
            sleep(1)
            print('Voltando...')
            sleep(1)
            verMedia()
        else:
            soma = 0
            for glicemia in dados.glicemias_07:
                soma += glicemia  # soma os valores das glicemias que estão na lista
            else:
                media = soma / len(dados.glicemias_07)  # faz a equação para fazer a média
                print(f'A sua média no periodo de "Depois do jantar" é {media:.0f}')
                sleep(1)
                print(f'Voltando para o menu principal...')
                sleep(1)
                glicemiaApp()
    elif escolha == '8':
        print('Você escolheu "Ao dormir".')
        if not dados.glicemias_08 or len(dados.glicemias_08) < 2:
            print(f'Ainda há {len(dados.glicemias_08)} glicemias atualmente...\n')
            sleep(1)
            print('Voltando...')
            sleep(1)
            verMedia()
        else:
            soma = 0
            for glicemia in dados.glicemias_08:
                soma += glicemia  # soma os valores das glicemias que estão na lista
            else:
                media = soma / len(dados.glicemias_08)  # faz a equação para fazer a média
                print(f'A sua média no periodo de "Ao dormir" é {media:.0f}')
                sleep(1)
                print(f'Voltando para o menu principal...')
                sleep(1)
                glicemiaApp()
    elif escolha == '9':
        print('Você escolheu "Sem Período Especificado".')
        if not dados.glicemias_09 or len(dados.glicemias_09) < 2:
            print(f'Ainda há {len(dados.glicemias_08)} glicemias atualmente...\n')
            sleep(1)
            print('Voltando...')
            sleep(1)
            verMedia()
        else:
            soma = 0
            for glicemia in dados.glicemias_09:
                soma += glicemia  # soma os valores das glicemias que estão na lista
            else:
                media = soma / len(dados.glicemias_09)  # faz a equação para fazer a média
                print(f'A sua média no periodo de "Sem Período Especificado" é {media:.0f}')
                sleep(1)
                print(f'Voltando para o menu principal...')
                sleep(1)
                glicemiaApp()
    elif escolha == 'q' or escolha == 'Q':
        fechaApp()
    elif escolha == 'r' or escolha == 'R':
        verMedia()
    elif escolha == 'v' or escolha == 'V':
        glicemiaApp()

    else:
        print('Algo deu errado, tente novamente!')
        sleep(1)
        verMedia()


def configs():  # Configurações avançadas Function
    print("\033[1;32m=\033[m" * 30)
    print('\033[1;32mBem Vindo(a) as Configurações Avançadas\033[m')
    print("\033[1;32m=\033[m" * 30, '\n')
    escolha = input('O que você quer fazer?\n\n'
                    'Alterar e-mail >>> 1\n'
                    'Alterar senha >>> 2\n'
                    'Apagar conta >> 3\n'
                    'Voltar ao Menu Anterior >> 4\n'
                    '>>> ')

    if escolha == '1':
        def altera_email():
            print('Você escolheu ALTERAR E-MAIL.\n'
                  'ATENÇÃO: Ao fazer a alteração de e-mail, você será redirecionado para a área de login!\n')
            volta = input('Se deseja voltar tecle "v" ou "c" para continuar.\n'
                          '>>> ')
            if volta == 'v' or volta == 'V':
                configs()
            elif volta == 'c':  # continuará caso o usuário
                def cont_alter():
                    email_atual = input('Digite seu e-mail atual: ')
                    if email_atual in dados.emails:
                        email_atualizado = input('Digite seu novo e-mail: ')
                        email_atualizado_valida = input('Novamente, digite seu novo e-mail: ')
                    else:
                        print(f'\nO e-mail: {email_atual} não está em nossas bases de dados, tente novamente.\n')
                        sleep(1)
                        cont_alter()
                    # Abaixo pergunta se o email tem @ e .com e se está válido
                    if email_atualizado == email_atualizado_valida and '@' and '.com' in email_atualizado:
                        dados.emails.remove(email_atual)  # remove o email da base de dados
                        dados.emails.append(email_atualizado)  # e adiciona o novo email à base de dados
                        print('E-mail atualizado com sucesso!\n\n'
                              'Você está sendo redirecionado para área de Login.\n')
                        sleep(2)
                        login()
                    else:
                        print(f'\nO e-mail "{email_atualizado}" não é válido! Tente novamente.\n')
                        sleep(1)
                        cont_alter()

                cont_alter()
            else:
                print('Algo deu errado, tente novamente!\n')
                sleep(1)
                altera_email()
        altera_email()  # executa a alteração de e-mail

    elif escolha == '2':
        def altera_senha():
            print('Você escolheu ALTERAR SENHA.\n'
                  'ATENÇÃO: Ao fazer a alteração de senha, você será redirecionado para a área de login!\n')
            volta = input('Se deseja voltar tecle "v" ou "c" para continuar.\n'
                          '>>> ')
            if volta == 'v' or volta == 'V':
                configs()
            elif volta == 'c' or volta == 'C':
                def cont_alter():
                    senha_atual = input('Digite sua senha atual: ')
                    if senha_atual in dados.senhas:
                        nova_senha = input('Digite a sua nova senha: ')
                        nova_senha_varifica = input('Digite novamente a sua nova senha: ')
                        if nova_senha == nova_senha_varifica:
                            def confim_alter():
                                confirma = input(f'\nConfirme a alteração da senha de:\n'
                                                 f'{senha_atual} para {nova_senha}\n'
                                                 f'(S) Para confirmar a alteração\n'
                                                 f'(N) Para alterar a nova senha.\n'
                                                 f'>>> ')
                                if confirma == 'S' or confirma == 's':
                                    print('Ok, alterando dados.')
                                    sleep(1)
                                    print(f'Removendo senha: "{senha_atual}"...')
                                    dados.senhas.remove(senha_atual)
                                    sleep(1)
                                    print(f'Adicionando senha: "{nova_senha}" ao banco de dados...')
                                    sleep(1)
                                    dados.senhas.append(nova_senha)
                                    print('Pronto, sua senha foi alterada com sucesso!\n\n'
                                          'Indo para o login.\n')
                                    login()
                                elif confirma == 'n' or confirma == 'N':
                                    print('Ok, voltando...')
                                    sleep(1)
                                    cont_alter()
                                else:
                                    print('Algo deu errado, tente novamente!')
                                    sleep(1)
                                    confim_alter()
                            confim_alter()
                        else:
                            print(f'As senhas não combinam. Tente novamente!')
                            sleep(1)
                            cont_alter()
                    else:
                        print(f'A senha que você digitou ({senha_atual}) é inválida. Tente novamente!')
                        sleep(1)
                        cont_alter()
                cont_alter()
            else:
                print('Algo deu errado, Tente novamente')
                sleep(1)
        altera_senha()
    else:
        print('Algo deu errado! Tente novamente.')
        sleep(1)
        configs()


def fechaApp():
    print('Tudo bem! Muito obrigado!')
    sleep(1)
    print('Saindo...')
    sleep(2)
    exit()


if __name__ == '__main__':
    inicio()

# Adicionar uma forma de mostrar a média da glicemia
