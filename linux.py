#!/usr/bin/env python3

import PySimpleGUI as sg

window = sg.Window('Window', layout=[[sg.Button('OK')]])

while True :
    event, values = window.read()

    if event == sg.WIN_CLOSED or event == 'OK' :
        break

window.close()
