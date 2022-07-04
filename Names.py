from time import sleep
from maskpass import askpass
from plyer import notification
import os

senha_real = "123"
contador_nomes = 0
lista_nomes = []

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
