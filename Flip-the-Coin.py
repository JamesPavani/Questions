import PySimpleGUI as sg
from time import sleep
from random import choice

CARA = str("Cara")
COROA = str("Coroa")

lista = [CARA, COROA]
resultado = choice(lista)

sg.theme("Reddit")

escolha = [
    [sg.Text("Escolha:"), sg.Button("CARA")],
    [sg.Text("        "), sg.Button("COROA")]
]

giro = [
    [sg.Button("Aperte para girar a moeda")]
]

de_novo = [
    [sg.Text("Deseja ir de novo?"), sg.Button("SIM"), sg.Button("NÃO")]
]

janela_escolha = sg.Window("CARA OU COROA", escolha)
janela_giro = sg.Window("CARA OU COROA", giro)
janela_de_novo = sg.Window("De novo?", de_novo)

while True:
    events1, values1 = janela_escolha.read()
    events2, values2 = janela_giro.read()
    events3, values3 = janela_de_novo()

    janela_giro.hide()
    janela_de_novo.hide()

    if events1 == "CARA" or events1 == "COROA":
        janela_escolha.hide()
        sleep(1)
        janela_giro.un_hide()

        if events2 == "Aperte para girar a moeda":
            janela_giro.hide()
            sleep(1)

            CARA = str("Cara")
            COROA = str("Coroa")

            lista = [CARA, COROA]
            resultado = choice(lista)

            if resultado == CARA:
                sg.popup("CARA")

            else:
                sg.popup("COROA")

            sleep(1)

            if events1 == "CARA" and resultado == COROA or events1 == "COROA" and resultado == CARA:
                sg.popup("Computador ganhou")

            if events1 == "CARA" and resultado == CARA or events1 == "COROA" and resultado == COROA:
                sg.popup("Você ganhou")

            sleep(1)

            janela_de_novo.un_hide()

            if events3 == "SIM":
                sleep(1)
                janela_escolha.un_hide()

            if events3 == "NÃO":
                sleep(1)
                break
sleep(1)
janela_escolha.close()
janela_giro.close()
janela_de_novo.close()
