from time import sleep
from random import choice
import os
import sys

casas = ["LUFA-LUFA", "SONSERINA", "GRIFINÓRIA", "CORVINAL"]

sorteio = choice(casas)

linha = str("-----------------------------------------------------\n")

def Primeiro_Diálogo():
    diálogo_um = str(f"- Ah, olá {primeiro_nome} {ultimo_nome}! Muito bom te ver por aqui... Deixe-me começar\n"
                     "a ler o que se passa dentro de sua mente por um momento. Mas, antes de\n"
                     "começarmos... Eu tenho uma pergunta para te fazer... Você tem preferência de alguma casa?")

    for du in diálogo_um:
        sys.stdout.write(du)
        sys.stdout.flush()
        sleep(0.1)

def Cabeçalho():

    os.system("cls")
    sleep(1)

    for l in linha:
        sys.stdout.write(l)
        sys.stdout.flush()
        sleep(0.1)
    sleep(1)

    print("|               CERIMÔNIA DE SELEÇÃO                |")
    sleep(1)

    for l in linha:
        sys.stdout.write(l)
        sys.stdout.flush()
        sleep(0.1)



while True:
    os.system("cls")
    sleep(1)

    primeiro_nome = str(input("Digite seu Primeiro Nome: ")).strip()
    ultimo_nome = str(input("Digite seu Último Nome: ")).strip()

    Cabeçalho()
    sleep(1)

    os.system("cls")
    Primeiro_Diálogo()
