def Level():
    while True:
        try:
            level = int(input('Choose your level: '))
            if level < 1:
                print("\033[31mLEVEL NOT VALID! CANNOT BE LESS THAN 1.\033[m")
            else:
                return level
        except ValueError:
            print('\033[31mINVALID DIGIT!\033[m')


def Pythonator(level):
    from time import sleep
    from random import randint

    engine = randint(1, level * 5)

    print(f'''
I am thinking in a number from \033[33m1 to {level * 5}\033[m! Try to guess it... ;)
''')
    
    sleep(1)

    tries = 1

    while True:
        try:
            player = int(input('\033[33mEnter your guess:\033[m '))
            
            if player == engine:
                break

            elif player > engine:
                print(f'''
The secret number is less than {player}... \033[35m<<<\033[m
''')

            else:
                print(f'''
The secret number is greater than {player}... \033[35m>>>\033[m
''')
            tries += 1

            sleep(1)
        
        except ValueError:
            print('\033[31mINVALID DIGIT!\033[m')

    if tries == 1:
        print('''\033[36m
Wow... You guessed the number in 1 try! Congratulations, clairvoyant!!!\033[m
''')
    else:
        print(f'''\033[32m
Congratulations! You guessed the number after \033[m{tries}\033[32m tries.\033[m
''')
    sleep(1)


def playAgain():
    from time import sleep

    while True:
        answer = input('Play again? [Y/N]: ').upper().strip()

        if answer != 'Y' and answer != 'N':
            print('\033[31mENTER A VALID ANSWER!\033[m')
        
        elif answer == 'N':
            return False
        
        else:
            print('''\033[33m
STARTING NEW GAME...
\033[m''')
            sleep(1)
            print('''\033[36m=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=
\033[m''')
            return True


def title():
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

<<< THANK YOU FOR PLAYING PYTHONATOR! UNTIL NEXT TIME :) >>>
\033[m''')
    sleep(1)
