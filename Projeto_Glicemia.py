from time import sleep

# db
email_db = 'gab'
nome_db = 'Gabriel'
senha_db = '123'
glicemia_list1 = []
glicemia_list2 = []
glicemia_list3 = []
glicemia_list4 = []
glicemia_list5 = []
glicemia_list6 = []
glicemia_list7 = []
glicemia_list8 = []
glicemia_list9 = []


# db
# Functions


# Functions
# inicio programa

pergunta = input('Você já tem cadastro?\nSim - 1\nNão - 2\n>>> ')  # pergunta se tem cadastro
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

glicemia = input('Coloque aqui a sua glicemia: ')

while not glicemia.isnumeric():
    print('O que você digitou, não é um número!')
    glicemia = input('Coloque aqui a sua glicemia: ')
else:
    glicemia = int(glicemia)

if glicemia >= 600 or glicemia <= 40:
    while glicemia >= 600 or glicemia <= 40:
        print('Valor muito alto ou baixo! Tente novamente!')
        glicemia = input('Coloque aqui a sua glicemia: ')
        if glicemia.isnumeric():
            glicemia = int(glicemia)
        else:
            while not glicemia.isnumeric():
                print('O que você digitou, não é um número!')
                glicemia = input('Coloque aqui a sua glicemia: ')
                if glicemia.isnumeric():
                    glicemia = int(glicemia)
                    break

escolha_periodo = input('Coloque o período da medição.\n'
                        'Ao levantar ➜ 1\n'
                        'Antes do almoço ➜ 2\n'
                        'Depois do almoço ➜ 3\n'
                        'Antes do lanche ➜ 4\n'
                        'Depois do lanche ➜ 5\n'
                        'Antes do jantar ➜ 6\n'
                        'Depois do jantar ➜ 7\n'
                        'Ao dormir ➜ 8\n'
                        'Sem Período especificado ➜ 9\n'
                        '>>> ')
if not escolha_periodo.isnumeric():
    while not escolha_periodo.isnumeric():
        print('Erro! tente novamente!')
        escolha_periodo = input('Coloque o período da medição.\n'
                                'Ao levantar ➜ 1\n'
                                'Antes do almoço ➜ 2\n'
                                'Depois do almoço ➜ 3\n'
                                'Antes do lanche ➜ 4\n'
                                'Depois do lanche ➜ 5\n'
                                'Antes do jantar ➜ 6\n'
                                'Depois do jantar ➜ 7\n'
                                'Ao dormir ➜ 8\n'
                                'Sem Período especificado ➜ 9\n'
                                '>>> ')
    else:
        escolha_periodo = int(escolha_periodo)
else:
    escolha_periodo = int(escolha_periodo)

while True:
    if escolha_periodo == 1:
        glicemia_list1.append(glicemia)
        print('Glicemia adicionada com sucesso!\n')
        print('Como periodo "Ao levantar"')
        sair = input('Você quer sair ou adicionar mais uma glicemia?\n'
                     'SAIR ➜ 1\n'
                     'ADICIONAR MAIS DADOS ➜ 2'
                     '>>> ')
        if sair != '1' or sair != '2':
            while sair != '1' or sair != '2':
                print('Não foi possível entender, tente novamente.')
                sair = input('Você quer sair ou adicionar mais uma glicemia?\n'
                             'SAIR ➜ 1\n'
                             'ADICIONAR MAIS DADOS ➜ 2'
                             '>>> ')
                if sair == '1' or sair == '2':
                    break
        elif sair == '1':
            break

    elif escolha_periodo == 2:
        glicemia_list2.append(glicemia)
        print('Glicemia adicionada com sucesso!\n')
        print('Como periodo "Antes do almoço"')
    elif escolha_periodo == 3:
        glicemia_list3.append(glicemia)
        print('Glicemia adicionada com sucesso!\n')
        print('Como periodo "Depois do almoço"')
    elif escolha_periodo == 4:
        glicemia_list4.append(glicemia)
        print('Glicemia adicionada com sucesso!\n')
        print('Como periodo "Antes do lanche"')
    elif escolha_periodo == 5:
        glicemia_list5.append(glicemia)
        print('Glicemia adicionada com sucesso!\n')
        print('Como periodo "Depois do lanche"')
    elif escolha_periodo == 6:
        glicemia_list6.append(glicemia)
        print('Glicemia adicionada com sucesso!\n')
        print('Como periodo "Antes do jantar"')
    elif escolha_periodo == 7:
        glicemia_list7.append(glicemia)
        print('Glicemia adicionada com sucesso!\n')
        print('Como periodo "Depois do jantar"')
    elif escolha_periodo == 8:
        glicemia_list8.append(glicemia)
        print('Glicemia adicionada com sucesso!\n')
        print('Como periodo "Ao dormir"')
    elif escolha_periodo == 9:
        glicemia_list9.append(glicemia)
        print('Glicemia adicionada com sucesso!\n')
        print('Como periodo "Sem periodo especificado"')
    else:
        print('Erro! Tente novamente!')
        escolha_periodo = input('Coloque o período da medição.\n'
                                'Ao levantar ➜ 1\n'
                                'Antes do almoço ➜ 2\n'
                                'Depois do almoço ➜ 3\n'
                                'Antes do lanche ➜ 4\n'
                                'Depois do lanche ➜ 5\n'
                                'Antes do jantar ➜ 6\n'
                                'Depois do jantar ➜ 7\n'
                                'Ao dormir ➜ 8\n'
                                'Sem Período especificado ➜ 9\n'
                                '>>> ')



        """
        Parei onde ao adicionar o periodo, entra em um loop infinito de adição na lista do periodo escolhido. deve-se 
        colocar break's para que na hora de adicionar, já quebre o loop
        """