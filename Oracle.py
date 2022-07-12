from random import choice, shuffle
from time import sleep
import os
import sys

SIM = str("Sim")
NAO = str("Não")

pensando = [SIM, NAO]

linha = str("-------------------------------------------------------\n")

proxima = str("|                    ATÉ A PRÓXIMA                    |\n")

dialogo_oraculo = str("|Oráculo: Olá, percebi que você está com uma dúvida...|\n"
                      "|Oráculo: Saiba que estou aqui para ajudá-lo.         |\n"
                      "|Oráculo: Me faça qualquer pergunta!                  |\n"
                      "|Oráculo: Que irei respondê-la com SIM ou NÃO...      |\n"
                      "|Oráculo: Vamos nessa!                                |\n")

resposta_sim = str("|Oráculo: Bem, me deixe analisar a pergunta....       |\n"
                   "|Oráculo: É uma pergunta intrigante.                  |\n"
                   "|Oráculo: Mas, de acordo com a minha visão do futuro! |\n"
                   "|Oráculo: A resposta é...                             |\n"
                   "|Oráculo: \033[1;34mSIM\033[m!                        |\n")

resposta_nao = str("|Oráculo: Bem, me deixe analisar a pergunta....       |\n"
                   "|Oráculo: É uma pergunta intrigante.                  |\n"
                   "|Oráculo: Mas, de acordo com a minha visão do futuro! |\n"
                   "|Oráculo: A resposta é...                             |\n"
                   "|Oráculo: \033[1;31mNÃO\033[m!                        |\n")

os.system("cls")

sleep(2)

for l in linha:
    sys.stdout.write(l)
    sys.stdout.flush()
    sleep(0.1)

for d in dialogo_oraculo:
    sys.stdout.write(d)
    sys.stdout.flush()
    sleep(0.2)

for l in linha:
    sys.stdout.write(l)
    sys.stdout.flush()
    sleep(0.1)

sleep(1)

os.system("cls")

sleep(1)

while True:

    pergunta = str(input("\033[34mDigite a sua pergunta para o \033[1;34mOráculo\033[m\033[34m:\033[m "))
    sleep(1)

    os.system("cls")

    sleep(1)

    shuffle(pensando)
    escolha = choice(pensando)

    for l in linha:
        sys.stdout.write(l)
        sys.stdout.flush()
        sleep(0.1)

    if escolha == "Sim":
        for s in resposta_sim:
            sys.stdout.write(s)
            sys.stdout.flush()
            sleep(0.2)

    if escolha == "Não":
        for n in resposta_nao:
            sys.stdout.write(n)
            sys.stdout.flush()
            sleep(0.2)

    for l in linha:
        sys.stdout.write(l)
        sys.stdout.flush()
        sleep(0.1)

    sleep(1)

    os.system("cls")

    sleep(1)

    continuar = str(input("Quer digitar outra pergunta? ")).strip().upper()[0]
    sleep(1)

    while continuar != "S" and continuar != "N":
        os.system("cls")

        print("\033[1;31mNÃO ENTENDI!!!!!\033[m")
        sleep(1)
        print("\033[1;31mPOR FAVOR, DIGITE DE NOVO!!\033[m")
        sleep(1)
        continuar = str(input("\033[1;31mQuer digitar outra pergunta? \033[m")).strip().upper()[0]
        sleep(1)

    if continuar == "S":
        os.system("cls")

    if continuar == "N":
        for l in linha:
            sys.stdout.write(l)
            sys.stdout.flush()
            sleep(0.1)

        for p in proxima:
            sys.stdout.write(p)
            sys.stdout.flush()
            sleep(0.2)

        for l in linha:
            sys.stdout.write(l)
            sys.stdout.flush()
            sleep(0.1)

        break
