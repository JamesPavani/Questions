from time import sleep
from maskpass import askpass
from plyer import notification
import os

senha_real = "Carmack93"
contador_nomes = 0
lista_nomes = []
maior_palavra = ""

os.system("cls")
sleep(2)

print("---------------------------------")
sleep(1)
print("|             SENHA             |")
sleep(1)
print("---------------------------------")
sleep(2)
senha_usuario = askpass(prompt = "|Digite a Senha: ", mask = "*")
sleep(1)
print("---------------------------------")
sleep(1)
print("|                               |")
sleep(1)
print("---------------------------------")

sleep(2)

os.system("cls")

sleep(2)

if senha_usuario == senha_real:
    print("---------------------------------")
    print("|          \033[32mSENHA ACEITA\033[m         |")
    print("---------------------------------")
    notification.notify(
        title = "Mensagem:",
        message = "Seja Bem-Vindo.",
        app_icon = "",
        timeout = 10
    )

    sleep(10)

    os.system("cls")

    sleep(2)

    while True:
        print("-----------------------------------")
        print("|             NOMES               |")
        print("-----------------------------------")
        sleep(1)
        nome_digitado = str(input("|Digite um Nome: "))
        sleep(1)
        pergunta = str(input("|Quer digitar outro Nome? "))[0].upper()
        contador_nomes += 1
        adicionar = lista_nomes.append(nome_digitado)
        if contador_nomes == 1:
            maior_palavra = nome_digitado
        else:
            if len(nome_digitado) > len(maior_palavra):
                maior_palavra = nome_digitado

        while pergunta != "S" and pergunta != "N":
            sleep(1)
            print(" ")
            sleep(2)

            print("-------------------------------")
            print("|", "           \033[31mERRO\033[m", "            |")
            print("-------------------------------")
            sleep(1)
            print("\033[31m|COMANDO INVÁLIDO\033[m")
            sleep(1)
            print("\033[31m|RESPONDA DE NOVO!\033[m")
            sleep(1)
            pergunta = str(input("|Quer digitar outro Nome? "))[0].upper()

        if pergunta == "S":
            os.system("cls")

        if pergunta == "N":
            sleep(1)
            print("-----------------------------------")
            sleep(1)
            print("|                                 |")
            sleep(1)
            print("-----------------------------------")

            sleep(2)

            os.system("cls")

            sleep(2)

            print("-----------------------------------")
            print("|          NOMES DIGITADOS        |")
            print("-----------------------------------")
            sleep(1)

            print(" ")

            sleep(2)

            print("-" * (len(maior_palavra) + 8))
            sleep(1)

            for n in lista_nomes:
                print("|", f"  {n: ^{len(maior_palavra)}}", "  |")
                sleep(1)
                print("-" * (len(maior_palavra) + 8))
                sleep(1)
            sleep(1)

            print(" ")

            sleep(2)

            print("------------------------------" + "-" * len(maior_palavra))
            sleep(1)
            print(f"|Maior nome digitado: {maior_palavra}.      |")
            sleep(1)
            print("------------------------------" + "-" * len(maior_palavra))
            sleep(1)

            print(" ")

            sleep(1)
            print("----------------------------------" + "-" * len(str(contador_nomes)))
            sleep(1)
            print(f"|Quantidade de nomes digitados: {contador_nomes}.|")
            sleep(1)
            print("----------------------------------" + "-" * len(str(contador_nomes)))
            sleep(5)

            os.system("cls")

            sleep(1)
            print("-----------------------------------")
            print("|        PROGRAMA ENCERRADO       |")
            print("-----------------------------------")
            break

if senha_usuario != senha_real:
    print("---------------------------------")
    print("|         \033[31mSENHA NEGADA\033[m          |")
    print("---------------------------------")
    notification.notify(
        title = "Aviso:",
        message = "Intruso detectado.",
        app_icon = "",
        timeout = 10
    )

    sleep(7)

    os.system("cls")

    print("-----------------------------------")
    print("|        \033[31mPROGRAMA BLOQUEADO\033[m       |")
    print("-----------------------------------")

sleep(2)
os.system("cls")
sleep(2)
