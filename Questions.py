from random import choice
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

    if window == janela1 and events == sg.WIN_CLOSED or window == janela1 and events == "SAIR" or window == janela2 and events == sg.WIN_CLOSED or window == janela2 and events == "NÃO":
        break
