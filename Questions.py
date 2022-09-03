from random import choice, shuffle
import PySimpleGUI as sg
from time import sleep
import os

os.system("cls")
sleep(1)

def Pergunta():
    sg.theme("DarkPurple1")

    layout_pergunta = [
        [sg.Text("Digite sua pergunta:")],
        [sg.InputText()],
        [sg.Button("RESPOSTA")],
        [sg.Button("SAIR")]
    ]

    return sg.Window("Pergunta", layout = layout_pergunta, finalize = True)

def Outra():
    sg.theme("DarkPurple1")

    layout_outra = [
        [sg.Text("Quer digitar outra pergunta?")],
        [sg.Text("                   "), sg.Button("SIM")],
        [sg.Text("                   "), sg.Button("NÃO")]
    ]

    return sg.Window("Outra?", layout = layout_outra, finalize = True)

janela1, janela2 = Pergunta(), None

while True:
    window, events, values = sg.read_all_windows()

    if window == janela1 and events == "RESPOSTA":
        janela1.hide()
        sleep(1)

        escolhendo = ["SIM", "NÃO"]
        shuffle(escolhendo)
        escolha = choice(escolhendo)

        sg.popup(f"{escolha}")
        sleep(1)

        janela2 = Outra()

    if window == janela2 and events == "SIM":
        janela2.hide()
        sleep(1)
        janela1.un_hide()

        escolhendo = ["SIM", "NÃO"]
        shuffle(escolhendo)
        escolha = choice(escolhendo)

    if window == janela1 and events == sg.WIN_CLOSED or window == janela1 and events == "SAIR" or window == janela2 and events == sg.WIN_CLOSED or window == janela2 and events == "NÃO":
        break
