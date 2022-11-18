"""
Make a GUI to manage items on a list

Instructions:
Make a GUI that has:
Input Element to enter values to add
Listbox Element that is 20 chars wide and 10 entries high
3 Buttons - Add, Delete, Exit
When the user clicks Add, add the value that is in the input element if there is one
When the user clicks Delete, delete the highlighted item in the listbox
When the user clicks Exit, quit the event loop
Listbox documentation:

https://pysimplegui.readthedocs.io/en/latest/call%20reference/#listbox-element
"""

import PySimpleGUI as sg

trees = ['birch', 'willow', 'hazel']

layout = [  [sg.Text('Manage a list')],
            [sg.Input(size=(15,1), key='-IP-')],   # Input element goes here
            [sg.Listbox(values= trees, size=(15, 15), key='-LBOX-')],   # Listbox goes here
            [sg.Button('Add', bind_return_key=True), sg.Button('Delete'), sg.Button('Exit')]]   # Your 3 buttons goes here

window = sg.Window('Listbox Exercise', layout)

while True:
    event, values = window.read()

    if event == sg.WIN_CLOSED or event == 'Exit':
        break

    if event == 'Add':
        trees.append(values['-IP-'])
        window['-LBOX-'].update(trees)

        # print(trees)

    elif event == 'Delete':
        trees.remove(values['-LBOX-'][0])
        window['-LBOX-'].update(trees)
        pass

    if event == 'Exit':
        window.close()

window.close()