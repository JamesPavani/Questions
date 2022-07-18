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

janela1, janela2 = Operação(), None

while True:
    window, events, values = sg.read_all_windows()

    if window == janela1 and events == "SOMAR" or window == janela1 and events == "SUBTRAIR" or window == janela1 and events == "MULTIPLICAR" or window == janela1 and events == "DIVIDIR":
        janela1.hide()
        janela2 = Números()

    if window == janela2 and events == "Calcular":
        janela2.hide()

    if window == janela1 and events == sg.WINDOW_CLOSED or window == janela2 and events == sg.WINDOW_CLOSED:
        break
