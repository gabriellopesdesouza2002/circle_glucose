import dados, circle_glucose
from time import sleep


def configsAvanc():
    escolha = input('O que você quer fazer?\n\n'
                    'Alterar e-mail >>> 1\n'
                    'Alterar senha >>> 2\n'
                    'Apagar conta >> 3\n'
                    '>>> ')

    if escolha == '1':
        def trocaEmail():
            email_atual = input('Digite seu e-mail atual: ')
            if email_atual in dados.emails:
                dados.emails.remove(email_atual)
            else:
                print('\nO E-mail não existe! Tente novamente.\nPor segurança faça o procedimento novamente!\n')
                configsAvanc()
            email_atualizado = input('Digite seu novo e-mail: ')
            if email_atualizado not in '@' and '.com':
                print('\nCadastre um e-mail válido!\nPor segurança faça o procedimento novamente!\n')
                configsAvanc()
            email_atualizado_valida = input('Novamente, digite seu novo e-mail: ')
            if email_atualizado == email_atualizado_valida:
                dados.emails.append(email_atualizado)
                print('E-mail atualizado com sucesso!')
                print('Sendo redirecionado para área de Login')
                sleep(2)
                circle_glucose.Login()
            else:
                print('\nE-mail diferente! Tente novamente.\nPor segurança faça o procedimento novamente!\n')
                trocaEmail()
    else:
        print('Algo deu errado! Tente novamente.')
        configsAvanc()