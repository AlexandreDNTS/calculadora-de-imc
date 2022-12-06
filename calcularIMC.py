import PySimpleGUI as sg

def tela_calculadoraIMC():
    layout=[
        [sg.Text('\t\tCalculadora IMC')],
        [sg.Text('PESO'),sg.Input(key='peso')],
        [sg.Text('ALTURA(m)'), sg.Input(key='altura')],
        [sg.Text('seu imc : ')],
        [sg.Text('',key='msg')],
        [sg.Button('CALCULAR IMC')]
    ]
    return sg.Window('CALCULAR IMC',layout=layout,finalize=True,size=(350,200))

calculadora = tela_calculadoraIMC()

while True:
    window,eventos,valores = sg.read_all_windows()

    if eventos == sg.WIN_CLOSED:
        break
    if  window == calculadora and eventos == 'CALCULAR IMC':
        peso=float(valores['peso'])
        altura=float(valores['altura'])
        IMC = peso/altura**2
        window['msg'].update(+IMC)
