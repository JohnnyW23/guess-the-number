from appModule import *

titulo()

while True:
    nivel = Nivel()

    Pythonator(nivel)

    if not playAgain():
        exit()
        break
