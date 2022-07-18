import PySimpleGUI as sg

def Operação():

    sg.theme("Reddit")

    layout_op = [
        [sg.Button("SOMAR")],
        [sg.Button("SUBTRAIR")],
        [sg.Button("MULTIPLICAR")],
        [sg.Button("DIVIDIR")]
    ]

    return sg.Window("Operação", layout_op, finalize = True)

def Números():

    sg.theme("Reddit")

    layout_num = [
        [sg.Text("Primeiro Número:"), sg.Input(size = (11, 1) )],
        [sg.Text("Segundo Número:"), sg.Input(size = (11, 1) )],
        [sg.Button("Calcular")]
    ]

    return sg.Window("Números", layout_num, finalize = True)

def De_novo():

    sg.theme("Reddit")

    layout_de_novo = [
        [sg.Text("Quer fazer outro cálculo?")],
        [sg.Button("SIM")],
        [sg.Button("NÃO")]
    ]

    return sg.Window("De novo?", layout_de_novo, finalize = True)

janela1, janela2, janela3 = Operação(), None, None

while True:
    window, events, values = sg.read_all_windows()

    if window == janela1 and events == "SOMAR" or window == janela1 and events == "SUBTRAIR" or window == janela1 and events == "MULTIPLICAR" or window == janela1 and events == "DIVIDIR":
        janela1.hide()
        eventos = events
        janela2 = Números()

    if window == janela2 and events == "Calcular":
        janela2.hide()

        if eventos == "SOMAR" and window == janela2:
            sg.popup(f"O resultado é: {int(values[0]) + int( values[1])}")
        if eventos == "SUBTRAIR" and window == janela2:
            sg.popup(f"O resultado é: {int(values[0]) - int( values[1])}")
        if eventos == "MULTIPLICAR" and window == janela2:
            sg.popup(f"O resultado é: {int(values[0]) * int(values[1])}")
        if eventos == "DIVIDIR" and window == janela2:
            sg.popup(f"O resultado é: {int(values[0]) / int(values[1])}")

        janela3 = De_novo()

    if window == janela3 and events == "SIM":
        janela3.hide()
        janela1.un_hide()

    if window == janela2 and events == "Calcular":
        janela2.hide()

    if window == janela1 and events == sg.WINDOW_CLOSED or window == janela2 and events == sg.WINDOW_CLOSED:
        break

    if window == janela3 and events == "NÃO" or window == janela3 and events == sg.WINDOW_CLOSED:
        break
