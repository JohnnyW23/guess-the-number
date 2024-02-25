def Nivel():
    while True:
        try:
            nivel = int(input('Escolha seu nível: '))
            if nivel < 1:
                print('\033[31mNÍVEL INVÁLIDO! NÃO PODE SER MENOR QUE 1.\033[m')
            else:
                return nivel
        except ValueError:
            print('\033[31mDIGITO INVÁLIDO!\033[m')


def Pythonator(nivel):
    from time import sleep
    from random import randint

    engine = randint(1, nivel * 5)

    print(f'''
Estou pensando em um número de \033[33m1 a {nivel * 5}\033[m! Tente adivinhar qual é... ;)
''')
    
    sleep(1)

    tentativas = 1

    while True:
        try:
            jogador = int(input('\033[33mDigite seu palpite:\033[m '))
            
            if jogador == engine:
                break

            elif jogador > engine:
                print(f'''
O número secreto é menor que {jogador}... \033[35m<<<\033[m
''')

            else:
                print(f'''
O número secreto é maior que {jogador}... \033[35m>>>\033[m
''')
            tentativas += 1

            sleep(1)
        
        except ValueError:
            print('\033[31mDIGITO INVÁLIDO!\033[m')

    if tentativas == 1:
        print('''\033[36m
Uau... Você adivinhou em 1 tentativa! Parabéns, vidente!!!\033[m
''')
    else:
        print(f'''\033[32m
Parabéns! Você adivinhou o número depois de \033[m{tentativas}\033[32m tentativas.\033[m
''')
    sleep(1)


def playAgain():
    from time import sleep

    while True:
        resp = input('Jogar novamente? [S/N]: ').upper().strip()

        if resp != 'S' and resp != 'N':
            print('\033[31mDÊ UMA RESPOSTA VÁLIDA!\033[m')
        
        elif resp == 'N':
            return False
        
        else:
            print('''\033[33m
INICIANDO NOVO JOGO...
\033[m''')
            sleep(1)
            print('''\033[36m=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=
\033[m''')
            return True


def titulo():
    from time import sleep

    print(f'''\033[36m
=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=
{'PYTHONATOR v1.0'.center(49)}
=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=
\033[m''')

    sleep(1)


def exit():
    from time import sleep
    print('''\033[36m
=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=

<<< OBRIGADO POR JOGAR PYTHONATOR! ATÉ A PRÓXIMA :) >>>
\033[m''')
    sleep(1)
