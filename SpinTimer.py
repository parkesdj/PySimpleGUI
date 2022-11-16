"""
Spin Element
Make a Timer GUI
Instructions:
You are making a GUI that will be used as a timer. Use 2 Spin Elements to enable your user to set the hours and minutes. Each should be values 0 to 59. You do not need to handle "rollover" for the minutes to hours.

There are 2 approaches you may take on this exercise:
1. Use Ints for the values 2. Use strings which will enable you to have leading zeros
In other words, a value of 0 hours and 0 minutes can look like this:
0 : 0
Or like this:
00 : 00

Make a window that has 3 rows
Row 1 should read "Timer GUI"
Row 2 will have your Spin Elements
Row 3 should have 2 buttons - "Set" and "Clear"
Button Operation
Set - Prints the values of the Spin elements in the Debug Window
Clear - Resets the value to 0 hours 0 minutes
Set the font for the entire Window to be "Courier" with a size of 40 so that it is easy to see and interact with.
Spin Element in the Call Reference Documentation
"""

import PySimpleGUI as sg

spinner_values = [f'{i:02}' for i in range(60)]
zero = '00'

layout = [[sg.Text('Timer GUI')],
          # Insert your Spin code here
          [sg.Spin(spinner_values, size=(2, 1), key='-Hours-'), sg.Text(':'),\
           sg.Spin(spinner_values, size=(2, 1), key='-Minutes-')],
          [sg.Button('Set'), sg.Button('Clear')]]  # and complete the reset of the layout

window = sg.Window('Timer', layout, font='Courier40')  # Add your layout and set the font

while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED:
        break
    if event == 'Set':
        sg.Print('Hours =', values['-Hours-'], 'Minutes =', values['-Minutes-'])
    if event == 'Clear':
        window['-Hours-'].update(zero)
        window['-Minutes-'].update(zero)
    # Add your code to handle events for buttons

window.close()
