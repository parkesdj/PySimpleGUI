"""
Make a GUI to select a "Player Character Type" for a game

Instructions:
You're making a game and the user has these choices of player types:

Warrior
Wizard
Ninja
Archer
Cleric
Make a window that uses Radio Buttons to enable players to choose a type.
All of the choices should be on 1 row in your Window.
Include 2 buttons
Ok - Shows a popup of the values dictionary returned from window.read()
Clear - Clears the choices
Radio Button in the Call Reference Documentation
"""
import PySimpleGUI as sg

# Character types:
# Warrior
# Wizard
# Ninja
# Archer
# Cleric

characters = ['Warrior',  'Wizard', 'Ninja', 'Archer', 'Cleric' ]

charout = []

layout = [[sg.Text('Character type:', font='Default 15')],
          # Your radio buttons will be in this part of the window
          [sg.Radio(char, group_id=1, k=char, enable_events=True) for char in characters],
          [sg.Button('Ok'), sg.Button('Clear')]]

window = sg.Window('Food Order GUI', layout)

while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED:
        break
    if event == 'Ok':
        for i in values:
            if values[i] == True:
                sg.popup(i, title='Values')
    if event == 'Clear':
        window['Warrior'].reset_group()

window.close()