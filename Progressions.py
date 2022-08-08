from time import sleep
import sys
import os

os.system("cls")
sleep(1)

def Menu():
    linha = str("------------------------------------------------------------\n")

    for l in linha:
        sys.stdout.write(l)
        sys.stdout.flush()
        sleep(0.15)

    sleep(1)
    print("|                        PROGRESSÕES                       |")
    sleep(1)

    for l in linha:
        sys.stdout.write(l)
        sys.stdout.flush()
        sleep(0.15)
    sleep(1)
    print("|[1] - Criar uma Progressão Aritmética.                    |")
    sleep(1)
    print("|[2] - Criar uma Progressão Geométrica.                    |")
    sleep(1)
    print("|[3] - Termo Geral da Progressão Aritmética.               |")
    sleep(1)
    print("|[4] - Termo Geral da Progressão Geométrica.               |")
    sleep(1)
    print("|[5] - Soma dos Termos da Progressão Aritmética.           |")
    sleep(1)
    print("|[6] - Soma dos Termos Finitos da Progressão Geométrica.   |")
    sleep(1)
    print("|[7] - Soma dos Termos Infinitos da Progressão Geométrica. |")
    sleep(1)

    for l in linha:
        sys.stdout.write(l)
        sys.stdout.flush()
        sleep(0.15)

Menu()
