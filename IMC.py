# CALCULADOR-DE-IMC

import PySimpleGUI as sg

sg.theme('DarkTeal2')

Luiz = [
  [sg.Text('IMC')],
  [sg.Text('Massa: '), sg.Input(key='-MASS-',size=(5,1))],
  [sg.Text('Altura: '),sg.Input(key='-HEIGHT-',size=(5,1))],
  [sg.Push(),sg.Button('calcular'),sg.Push()]
  
  ]

window = sg.Window('IMC', layout=Luiz, font='Monaco 18')

while True:
  event, value = window.read()
  massa=float(value['-MASS-'])
  altura=float(value['-HEIGHT-'])
  IMC= massa/ altura**2
  if IMC>=20 and IMC<=25: 
    msg='Você esta no peso ideal para sua altura'
  elif IMC<20: 
    msg='Você esta abaixo do peso para sua altura'
  else:
      msg='Você esta acima do peso para sua altura'
  sg.Popup('IMC, resultado',f'Seu imc é {IMC:.2f}\n {msg}')
  if event== 'QUIT' or event == sg.WIN_CLOSED:
    break
