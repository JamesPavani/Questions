from time import sleep
import os
import sys

linha = str("-------------------------------------------------------\n")
dialogo_oraculo = str("|Oráculo: Olá, percebi que você está com uma dúvida...|\n"
                      "|Oráculo: Saiba que estou aqui para ajudá-lo.         |\n"
                      "|Oráculo: Me faça qualquer pergunta!                  |\n"
                      "|Oráculo: Que irei respondê-la com SIM ou NÃO...      |\n"
                      "|Oráculo: Vamos nessa!                                |\n")

os.system("cls")

sleep(2)

for l in linha:
    sys.stdout.write(l)
    sys.stdout.flush()
    sleep(0.1)

for d in dialogo_oraculo:
    sys.stdout.write(d)
    sys.stdout.flush()
    sleep(0.25)

for l in linha:
    sys.stdout.write(l)
    sys.stdout.flush()
    sleep(0.1)
