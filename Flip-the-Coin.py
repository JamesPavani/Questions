import PySimpleGUI as sg
from random import choice, shuffle

def escolha():
    sg.theme("Reddit")

    layout_escolha = [
        [sg.Text("Escolha:")],
        [sg.Button("CARA")],
        [sg.Button("COROA")]
    ]

    return sg.Window("Escolha", layout_escolha, finalize = True)

def giro():
    sg.theme("Reddit")

    layout_giro = [
        [sg.Button("Aperte para girar a moeda")]
    ]

    return sg.Window("Giro", layout_giro, finalize = True)

def de_novo():
    sg.theme("Reddit")

    layout_de_novo = [
        [sg.Text("Deseja ir girar de novo?"), sg.Button("SIM"), sg.Button("NÃO")]
    ]

    return sg.Window("De novo?", layout_de_novo, finalize = True)

janela1, janela2, janela3 = escolha(), None, None

while True:

    window, events, values= sg.read_all_windows()

    if window == janela1 and events == "CARA" or window == janela1 and events == "COROA":
        janela1.hide()
        eventos = events
        janela2 = giro()

    if window == janela2 and events == "Aperte para girar a moeda":
        janela2.hide()

        lista = ["Cara", "Coroa"]
        shuffle(lista)
        escolha = choice(lista)

        if escolha == "Cara":
            sg.popup("CARA")
            if eventos == "CARA":
                sg.popup("VOCÊ GANHOU")
            if eventos == "COROA":
                sg.popup("VOCÊ PERDEU")

        if escolha == "Coroa":
            sg.popup("COROA")
            if eventos == "COROA":
                sg.popup("VOCÊ GANHOU")
            if eventos == "CARA":
                sg.popup("VOCÊ PERDEU")

        janela3 = de_novo()

    if window == janela3 and events == "SIM":
        janela3.hide()
        janela1.un_hide()

    if window == janela1 and events == sg.WIN_CLOSED:
        break

    if window == janela2 and events == sg.WIN_CLOSED:
        break

    if window == janela3 and events == "NÃO":
        break
