from appModule import *

title()

while True:
    level = Level()

    Pythonator(level)

    if not playAgain():
        exit()
        break
