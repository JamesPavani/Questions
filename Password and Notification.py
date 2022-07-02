from time import sleep
from plyer import notification
from maskpass import askpass

senha_real = 749

print("---------------------------------")
sleep(1)
print("|             SENHA             |")
sleep(1)
print("---------------------------------")
sleep(2)
senha_digitada = int(askpass(prompt = "|Digite a Senha: ", mask = "*"))
sleep(2)
print("---------------------------------")
sleep(1)
print("|                               |")
sleep(1)
print("---------------------------------")
sleep(1)

print(" ")
sleep(2)

if senha_digitada == senha_real:
    print("---------------------------------")
    print("|", "\033[1;32m         SENHA ACEITA\033[m", "        |")
    print("---------------------------------")

    notification.notify(
        title = "Mensagem:",
        message = "Bem-Vindo.",
        app_icon = "",
        timeout = 10
    )

if senha_digitada != senha_real:
    print("---------------------------------")
    print("|", "\033[1;31m         SENHA NEGADA\033[m", "        |")
    print("---------------------------------")

    notification.notify(
        title = "Aviso:",
        message = "Intruso detectado.",
        app_icon = "",
        timeout = 10
    )
